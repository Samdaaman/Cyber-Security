class Stack:
    def __init__(self):
        self._stack = []

    def push(self, obj):
        self._stack.append(obj)

    def pop(self):
        if len(self._stack) > 0:
            top = self._stack[len(self._stack) - 1]
            self._stack.remove(top)
            return top

    def not_empty(self):
        return len(self._stack) > 0

    def get_all(self):
        return self._stack
