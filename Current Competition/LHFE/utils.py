import lhfe
from exceptions import FatalException


def debug(string: str):
    if lhfe.Instance is None:
        raise FatalException('Instance not set yet')
    else:
        if lhfe.Instance.debug:
            print(string)
