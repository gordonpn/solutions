class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == 1:
            if self.stack[0] < x:
                self.stack.insert(0, x)
            else:
                self.stack.append(x)
        elif len(self.stack) > 1:
            if x > self.stack[0]:
                self.stack.insert(0, x)
            elif x < self.stack[-1]:
                self.stack.append(x)
            else:
                index = 0
                while index + 1 < len(self.stack):
                    print(f"Comparing {x} >= {self.stack[index+1]}")
                    if x >= self.stack[index + 1] == True:
                        self.stack.insert(index, x)
                    index += 1
        elif not self.stack:
            self.stack.append(x)
        print(f"Pushed {x} - Stack: {self.stack}")

    def pop(self) -> None:
        print(f"Popping {self.stack[-1]}")
        self.stack.pop(-1)

    def top(self) -> int:
        value = self.stack[-1]
        print(f"Popping {value}")
        self.stack.pop(-1)
        return value

    def getMin(self) -> int:
        return self.stack[-1]


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3, "getMin() should be -3"
    minStack.pop()
    assert minStack.top() == -2, "Top should return -2"
    assert minStack.getMin() == 0, "getMin() should be 0"
    minStack.push(15)
    minStack.push(-9)
    minStack.push(-3)
    minStack.push(5)
    minStack.push(4)
    minStack.push(-2)
