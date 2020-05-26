class FatalException(Exception):
    def __init__(self, *args):
        if self.args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'Fatal Exception: {self.message}'
        else:
            return 'Unknown Fatal Exception'


class PathMissingException(FatalException):
    def __init__(self, path):
        self.message = f'Missing required path {path}'
