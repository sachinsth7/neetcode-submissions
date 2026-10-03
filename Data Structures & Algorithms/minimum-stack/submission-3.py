class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_value:
            self.min_value.append(val)
        else:
            self.previous_min = self.min_value[-1]
            self.new_min = min(val, self.previous_min)
            self.min_value.append(self.new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_value.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_value[-1]
