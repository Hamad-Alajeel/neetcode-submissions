# I need to remember the history of minimums across time. This can be done, by additionally storing information about the stack.


class MinStack:

    def __init__(self):
        self.stack = []
        self.history = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        last_cur_min = self.history[-1] if self.history else float("inf")
        if val <= last_cur_min:
            self.history.append(val)
        else:
            self.history.append(last_cur_min)
        return None

    def pop(self) -> None:
        self.history.pop()
        self.stack.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.history[-1]
