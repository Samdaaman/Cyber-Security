from .classes import TargetTracker

target_tracker = TargetTracker()
debug = None


def dprint(string: str) -> None:
    if debug:
        print(string)
