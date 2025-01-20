class MyQueue:
    def __init__(self):
        # Initialize two stacks
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        # Push an element onto the end of the queue
        self.in_stack.append(x)

    def pop(self) -> int:
        # Pop an element from the start of the queue
        self._shift_stacks()
        return self.out_stack.pop()

    def peek(self) -> int:
        # Get the front element
        self._shift_stacks()
        return self.out_stack[-1]

    def empty(self) -> bool:
        # Return True if the queue is empty, False otherwise
        return not self.in_stack and not self.out_stack

    def _shift_stacks(self):
        # Move elements from in_stack to out_stack if out_stack is empty
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

# The MyQueue object will be instantiated and called as following:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()