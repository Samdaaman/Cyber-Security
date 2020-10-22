import LoginToHTS
from Crypto.Cipher import Blowfish
import hashlib
import binascii


def get_data_list(phpssessid):
    # set level url
    levelurl = "https://www.hackthissite.org/missions/prog/9/"

    # get the content of the page
    content = LoginToHTS.login_and_get_with_phpsessid(levelurl, phpssessid)
    content_list = [line for line in content.split('/>')]

    soduku_untrimmed = ""
    blowfish_untrimmed = ""
    for content_item in content_list:
        if "Puzzle, in copy/paste form:" in content_item:
            soduku_untrimmed = content_item
        if "Blowfish encrypted string:" in content_item:
            blowfish_untrimmed = content_item

    soduku_trimmed = soduku_untrimmed.split("\"")[len(soduku_untrimmed.split("\"")) - 2]
    soduku_list = []
    for item in soduku_trimmed.split(","):
        if item != "":
            soduku_list.append(int(item))
        else:
            soduku_list.append(0)

    print("Got Sudoku")

    blowfish_almost_trimmed = blowfish_untrimmed[28:]
    blowfish_trimmed = blowfish_almost_trimmed[:len(blowfish_almost_trimmed) - 4]
    print("Got Blowfish: \"{}\"".format(blowfish_trimmed))

    return [soduku_list, blowfish_trimmed]

    # LoginToHTS.close_connection()


def setup_solve(starting_soduku_list):
    # add in all possibilities
    soduku_ints_possibilities = [[-1] for i in range(81)]
    for i in range(81):
        soduku_int = starting_soduku_list[i]
        if not soduku_int:
            soduku_ints_possibilities[i] = [j + 1 for j in range(9)]

    # code for random only
    # return solve_random(starting_soduku_list, soduku_ints_possibilities, [], 0)

    # code for smart + random
    return solve_soduku(starting_soduku_list, soduku_ints_possibilities)


def solve_soduku(starting_soduku_list, soduko_posibilities_list):
    # setup this_soduku
    this_soduku = starting_soduku_list.copy()

    soduku_ints_possibilities = soduko_posibilities_list.copy()

    last_soduku = []
    counter = 0
    while last_soduku != this_soduku:
        last_soduku = this_soduku.copy()
        solve_step(this_soduku, soduku_ints_possibilities)
        counter += 1

    if 0 in this_soduku:
        # start random cracker(multiple possibilites)
        random_solved_sodukus = solve_random(this_soduku, soduku_ints_possibilities, [], 0)
        return random_solved_sodukus
    else:
        # return
        return [this_soduku]


def solve_step(soduku_ints, soduku_ints_possibilites):
    # solve each horizontal
    for i in range(9):
        horizontal_ints = soduku_ints[i * 9: i * 9 + 9]
        horizontal_possibilites = soduku_ints_possibilites[i * 9: i * 9 + 9]

        # try solve the nine
        solved_nine_result = solve_nine(horizontal_possibilites, horizontal_ints)

        # if the possiblities were altered
        if len(solved_nine_result) >= 1:
            # set the new horizontal possibilities
            horizontal_possibilites = solved_nine_result[0]
            for j in range(9):
                horizontal_possibility = horizontal_possibilites[j]
                soduku_ints_possibilites[i * 9 + j] = horizontal_possibility

        # if the solved values were altered
        if len(solved_nine_result) == 2:
            # set the new values
            horizontal_ints = solved_nine_result[1]
            for j in range(9):
                horizontal_int = horizontal_ints[j]
                soduku_ints[i * 9 + j] = horizontal_int

    # solve vertical
    for i in range(9):
        vertical_ints = []
        vertical_possibilities = []
        for j in range(9):
            vertical_ints.append(soduku_ints[j * 9 + i])
            vertical_possibilities.append(soduku_ints_possibilites[j * 9 + i])

        # try solve the nine
        solved_nine_result = solve_nine(vertical_possibilities, vertical_ints)

        # if the possiblities were altered
        if len(solved_nine_result) >= 1:
            # set the new vertical possibilities
            vertical_possibilities = solved_nine_result[0]
            for j in range(9):
                vertical_possibility = vertical_possibilities[j]
                soduku_ints_possibilites[j * 9 + i] = vertical_possibility

        # if the solved values were altered
        if len(solved_nine_result) == 2:
            # set the new values
            vertical_ints = solved_nine_result[1]
            for j in range(9):
                vertical_int = vertical_ints[j]
                soduku_ints[j * 9 + i] = vertical_int

    # solve squares
    for i in range(9):
        box_ints = []
        box_possibilities = []
        for j in range(9):
            box_ints.append(soduku_ints[(i % 3) * 3 + (i // 3) * 27 + (j % 3) + (j // 3) * 9])
            box_possibilities.append(soduku_ints_possibilites[(i % 3) * 3 + (i // 3) * 27 + (j % 3) + (j // 3) * 9])

        # try solve the nine
        solved_nine_result = solve_nine(box_possibilities, box_ints)

        # if the possiblities were altered
        if len(solved_nine_result) >= 1:
            # set the new box possibilities
            box_possibilities = solved_nine_result[0]
            for j in range(9):
                box_possibility = box_possibilities[j]
                soduku_ints_possibilites[(i % 3) * 3 + (i // 3) * 27 + (j % 3) + (j // 3) * 9] = box_possibility

        # if the solved values were altered
        if len(solved_nine_result) == 2:
            # set the new values
            box_ints = solved_nine_result[1]
            for j in range(9):
                box_int = box_ints[j]
                soduku_ints[(i % 3) * 3 + (i // 3) * 27 + (j % 3) + (j // 3) * 9] = box_int


def solve_nine(nine_lists_possibilites, nine_ints_solved):
    nine_lists_processed = nine_lists_possibilites.copy()
    nine_ints_processed = nine_ints_solved.copy()

    # remove unnecessary possibilities from the lists
    for i in range(9):
        # for each value in the nine
        list_to_solve = nine_lists_processed[i].copy()
        if list_to_solve != [-1]:
            # for each possibility the value can't be
            for actual_value in nine_ints_processed:
                if actual_value in list_to_solve:
                    list_to_solve.remove(actual_value)
            if len(list_to_solve) == 1:
                # we have a value on its own
                nine_lists_processed[i] = list([-1])
                nine_ints_processed[i] = list_to_solve[0]
            else:
                # we just culled possibilities
                nine_lists_processed[i] = list_to_solve

    if nine_lists_processed != nine_lists_possibilites:
        # we altered the possibilites

        if nine_ints_processed != nine_ints_solved:
            # added a new solved value as well
            return [nine_lists_processed, nine_ints_processed]
        else:
            # we didnt add a new solved value
            return [nine_lists_processed]
    else:
        # we didn't change anything
        return ""


def solve_random(soduku_ints_list, sokuku_possibilites_list, solved_sodukus, current_index):
    # find first possibility to randomise
    index_to_randomise = 0
    for i in range(81 - current_index):
        if sokuku_possibilites_list[i + current_index] != [-1]:
            index_to_randomise = int(i + current_index)
            break

    # setup copies of varibles
    test_sudoku_possibilites = sokuku_possibilites_list.copy()
    test_sudoku_possibilites[index_to_randomise] = [-1]
    test_sudoku = soduku_ints_list.copy()

    # randomise possibility with for loop
    possibilities_to_randomise = sokuku_possibilites_list[index_to_randomise]
    for possible_value in possibilities_to_randomise:
        test_sudoku[index_to_randomise] = possible_value

        result_check = check_canidate(test_sudoku)
        # check if it is a correct sudoku
        if not result_check:
            continue

        # if soduku is done (2=done, 1=almost done, 0=invalid)
        if result_check == 2:
            # once code is complete add solved suduko to list
            if test_sudoku not in solved_sodukus:
                solved_sodukus.append(test_sudoku.copy())
            return solved_sodukus

        solve_random(test_sudoku, test_sudoku_possibilites, solved_sodukus, index_to_randomise)

    return solved_sodukus


def check_canidate(canidate_sudoku):
    # check horizontals
    for i in range(9):
        if not check_nine(canidate_sudoku[i * 9: i * 9 + 9]):
            # invalid canidate
            return 0

    # check verticals
    for i in range(9):
        if not check_nine([canidate_sudoku[j * 9 + i] for j in range(9)]):
            # invalid canidate
            return 0

    # check horizontals
    for i in range(9):
        if not check_nine([canidate_sudoku[(i % 3) * 3 + (i // 3) * 27 + (j % 3) + (j // 3) * 9] for j in range(9)]):
            # invalid canidate
            return 0

    if 0 in canidate_sudoku:
        # needs more solving
        return 1
    else:
        # fully solved
        return 2


def check_nine(nine_ints_list):
    for i in range(8):
        for j in range(8 - i):
            if nine_ints_list[i] == nine_ints_list[i + j + 1] and nine_ints_list[i]:
                # invalid canidate
                return 0

    # valid canidate but might be incomplete (have zeros)
    return 1


def decrypt_with_sodukukey(cipher_text, soduku):
    soduku_str = ""
    for number in soduku:
        soduku_str = soduku_str + number.__str__() + ","

    bs = 8
    key = hashlib.sha1(soduku_str.encode("utf-8")).digest()
    ciphertext = binascii.a2b_base64(cipher_text)
    iv = ciphertext[:bs]
    ciphertext = ciphertext[bs:]

    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    plain = cipher.decrypt(ciphertext)
    print(plain)
    print(binascii.b2a_base64(plain))
    return binascii.b2a_base64(plain).decode("utf-8")


def run():
    # # test soduku
    test_soduku_list = [4, 5, 6, 0, 2, 3, 9, 0, 0, 1, 0, 0, 0, 8, 9, 6, 5, 0, 7, 8, 9, 0, 5, 6, 3, 2, 0, 0, 9, 1, 5, 6, 0, 4, 0, 2, 0, 3, 4, 8, 0, 1, 0, 6, 0, 5, 6, 7, 0, 3, 4, 1, 9, 8, 0, 0, 0, 6, 7, 0, 0, 4, 0, 3, 4, 5, 9, 0, 2, 8, 0, 6, 0, 0, 8, 0, 0, 5, 0, 1, 9]

    solved_sodukus = setup_solve(test_soduku_list)
    for solved_soduku in solved_sodukus:
        for i in range(9):
            horzontal_row = solved_soduku[i * 9: i * 9 + 9]
            print(horzontal_row)
        print("\n")
    print("Done")

    # phpsessid = input("Enter PHPSESSID: ")
    # data = get_data_list(phpsessid)
    # soduku_unsolved = data[0]
    # cipher_text = data[1]
    #
    # soduku_str = input("Paste Sudoku: ")
    # soduku_unsolved = []
    # for item in soduku_str.split(","):
    #     if item != "":
    #         soduku_unsolved.append(int(item))
    #     else:
    #         soduku_unsolved.append(0)
    # solved_sodukus = setup_solve(soduku_unsolved)
    #
    # cipher_text = input("Paste Cipher_text: ")
    #
    # for solved_soduku in solved_sodukus:
    #     plain_text = decrypt_with_sodukukey(cipher_text, solved_soduku)
    #     print("\"{}\"".format(plain_text))


if __name__ == "__main__":
    run()
