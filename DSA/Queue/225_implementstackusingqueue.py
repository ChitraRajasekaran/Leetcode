from collections import deque

class MyStack:
    def __init__(self):
        # Use two queues to implement the stack behavior
        self.main_queue = deque()
        self.helper_queue = deque()

    def push(self, x: int) -> None:
        # Always push the new element to the helper_queue
        self.helper_queue.append(x)
        # Transfer all existing elements from the main_queue to the helper_queue
        while self.main_queue:
            self.helper_queue.append(self.main_queue.popleft())
        # Swap the references of the two queues to make helper_queue the new main_queue
        self.main_queue, self.helper_queue = self.helper_queue, self.main_queue

    def pop(self) -> int:
        # Remove and return the last pushed element which is at the start of the main_queue
        return self.main_queue.popleft()

    def top(self) -> int:
        # Return the last pushed element without removing it, which is at the start of the main_queue
        return self.main_queue[0]

    def empty(self) -> bool:
        # Check whether the main_queue is empty or not
        return len(self.main_queue) == 0

# Usage example
# stack = MyStack()
# stack.push(1)
# stack.push(2)
# print(stack.top())    # Returns 2
# print(stack.pop())    # Returns 2
# print(stack.empty())  # Returns False
