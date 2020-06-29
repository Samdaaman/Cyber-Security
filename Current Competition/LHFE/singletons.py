from .classes import TargetStack

target_stack = TargetStack()
debug = None


def dprint(string: str) -> None:
    if debug:
        print(string)
