class MyStack:

    def __init__(self):
        self.MyStack = []

    def push(self, x: int) -> None:
        self.MyStack.append(x)

    def pop(self) -> int:
        if self.MyStack:  # Ensure there are elements to pop
            return self.MyStack.pop()
        raise IndexError("Pop from an empty stack")

    def top(self) -> int:
        return self.MyStack[-1]

    def empty(self) -> bool:
        return not self.MyStack
        
