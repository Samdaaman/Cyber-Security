import os
import shutil
from typing import List
from PIL import Image
from .classes import Recipe, Target, RecipeOutput
from .constants import GEN_PREFIX, QUALITY, ALL_EXTENSION
from .incoming import enum_and_add_targets
from .processing import run_shell_command

_IMG_EXTENSIONS = ['gif', 'png', 'jpg', 'jpeg', 'png', 'bmp']


def run_all_for_target(target: Target) -> List[RecipeOutput]:
    output_list = []
    for recipe in all_recipes:
        if ALL_EXTENSION in recipe.applicable_extensions or target.extension in recipe.applicable_extensions:
            output = recipe.run(target)  # type: RecipeOutput
            output_list.append(output)
    return output_list


class FileRecipe(Recipe):
    def __init__(self):
        super(FileRecipe, self).__init__('File recipe', [ALL_EXTENSION])

    def run(self, target: Target) -> RecipeOutput:
        command = f'file {target.rel_path}'
        recipe_output = RecipeOutput(self, command)
        run_shell_command(self.name, recipe_output, False, command)
        return recipe_output


class HeadRecipe(Recipe):
    def __init__(self):
        super(HeadRecipe, self).__init__('Head recipe', [ALL_EXTENSION])

    def run(self, target: Target) -> RecipeOutput:
        command = f'xxd {target.rel_path} | head -n 40'
        recipe_output = RecipeOutput(self, command)
        run_shell_command(self.name, recipe_output, False, command)
        return recipe_output


class TailRecipe(Recipe):
    def __init__(self):
        super(TailRecipe, self).__init__('Tail recipe', [ALL_EXTENSION])

    def run(self, target: Target) -> RecipeOutput:
        command = f'xxd {target.rel_path} | tail -n 40'
        recipe_output = RecipeOutput(self, command)
        run_shell_command(self.name, recipe_output, False, command)
        return recipe_output


class StringsLongRecipe(Recipe):
    def __init__(self):
        super(StringsLongRecipe, self).__init__('Strings (Long) recipe', [ALL_EXTENSION])

    def run(self, target: Target) -> RecipeOutput:
        command = f'strings {target.rel_path} -n 8'
        recipe_output = RecipeOutput(self, command)
        run_shell_command(self.name, recipe_output, False, command, 50)
        return recipe_output


class StringsAllRecipe(Recipe):
    def __init__(self):
        super(StringsAllRecipe, self).__init__('Strings (All) recipe', [ALL_EXTENSION])

    def run(self, target: Target) -> RecipeOutput:
        command = f'strings {target.rel_path}'
        recipe_output = RecipeOutput(self, command)
        run_shell_command(self.name, recipe_output, True, command, 50)
        return recipe_output

class ExiftoolRecipe(Recipe):
    def __init__(self):
        super(ExiftoolRecipe, self).__init__('Exiftool recipe', [ALL_EXTENSION])
    
    def run(self, target: Target) -> RecipeOutput:
        command = f'exiftool {target.rel_path}'
        recipe_output = RecipeOutput(self, command)
        run_shell_command(self.name, recipe_output, True, command, 100)
        return recipe_output


# Image recipes
class BinwalkRecipe(Recipe):
    def __init__(self):
        super(BinwalkRecipe, self).__init__('Binwalk recipe', _IMG_EXTENSIONS)

    def run(self, target: Target) -> RecipeOutput:
        out_path = os.path.join(os.path.dirname(target.rel_path), f'{GEN_PREFIX}binwalk_{target.file_name}')
        command = f'binwalk -e {target.rel_path} --directory "{out_path}"'
        recipe_output = RecipeOutput(self, command)
        run_shell_command(self.name, recipe_output, False, command)

        if os.path.isdir(out_path) and len(os.listdir(out_path)) > 0:
            recipe_output.quality = QUALITY.MEDIUM
            nested_out_path = os.path.join(out_path, os.listdir(out_path)[0])
            files_to_move = os.listdir(nested_out_path)
            for file_to_move in files_to_move:
                shutil.move(os.path.join(nested_out_path, file_to_move), os.path.join(out_path, file_to_move))
            os.rmdir(nested_out_path)
            enum_and_add_targets(out_path, parent_target=target)
        elif os.path.isdir(out_path):
            recipe_output.quality = QUALITY.LOW
            os.rmdir(out_path)
        else:
            recipe_output.quality = QUALITY.LOW
        return recipe_output


class StegSolveRecipe(Recipe):
    def __init__(self):
        super(StegSolveRecipe, self).__init__('StegSolve image recipe', _IMG_EXTENSIONS)

    def run(self, target: Target) -> RecipeOutput:
        rel_path = f'{GEN_PREFIX}stegsolve_{target.file_name}'
        out_path = os.path.join(target.folder, rel_path)
        if not os.path.isdir(out_path):
            os.mkdir(out_path)
        recipe_output = RecipeOutput(self, 'Uses custom stegsolve python module')
        try:
            # open the image
            img_orig = Image.open(target.rel_path)
            width = img_orig.width
            height = img_orig.height
            # get the pixel data
            pxl_data = img_orig.load()

            # perform steg on each channel
            for channel in img_orig.mode:
                channel_index = img_orig.mode.index(channel)
                # for each plane on a certain channel
                for plane_number in range(8):
                    # get the plane
                    img_plane = Image.new('1', [width, height])
                    new_img_pxl_values = img_plane.load()
                    # go over each pixel in the image
                    for x in range(width):
                        for y in range(height):
                            pixel_value_colour = pxl_data[x, y]
                            if isinstance(pixel_value_colour, int):
                                pixel_value_channel = pixel_value_colour
                            else:
                                pixel_value_channel = pixel_value_colour[channel_index]
                            pixel_value_channel_bin = bin(pixel_value_channel)[2:].zfill(8)
                            pixel_value_plane = pixel_value_channel_bin[7 - plane_number]
                            new_img_pxl_values[x, y] = 255 * int(pixel_value_plane),
                    # save the image
                    filename = f'{img_orig.mode[channel_index]}_{plane_number}.png'
                    img_plane.save(os.path.join(out_path, filename))
                    recipe_output.add_image_path(os.path.join(rel_path, filename))

                # get the overall channel image
                img_overall = Image.new('L', [width, height])
                new_img_pxl_values = img_overall.load()
                # go over each pixel
                for x in range(width):
                    for y in range(height):
                        pixel_value_colour = pxl_data[x, y]
                        if isinstance(pixel_value_colour, int):
                            pixel_value_channel = pixel_value_colour
                        else:
                            pixel_value_channel = pixel_value_colour[channel_index]
                        new_img_pxl_values[x, y] = int(pixel_value_channel)
                # save the image
                filename = f'{img_orig.mode[channel_index]}_Overall.png'
                img_overall.save(os.path.join(out_path, filename))
                recipe_output.add_image_path(os.path.join(rel_path, filename))

        except KeyboardInterrupt as ex:
            recipe_output.add_output('Error occurred:')
            for arg in ex.args:
                recipe_output.add_output(f'Error: {arg}')
        else:
            recipe_output.add_output('Completed successfully')

        if len([file for file in os.scandir(out_path)]) == 0:
            os.rmdir(out_path)
        return recipe_output


all_recipes = [
    FileRecipe(),
    HeadRecipe(),
    TailRecipe(),
    BinwalkRecipe(),
    ExiftoolRecipe(),
    StegSolveRecipe(),
    StringsLongRecipe(),
    StringsAllRecipe()
]
