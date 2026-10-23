"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # New values are added to the top, so the newest value is removed first.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek inspects the top value without removing it.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New values join the back, while older values remain at the front.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front inspects the next value to be served without removing it.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO: TEXT EDITOR UNDO HISTORY ===")
    history = Stack()

    for action in [
        "Type title",
        "Add paragraph",
        "Insert image",
        "Fix spelling"
    ]:
        history.push(action)
        print(f"Added editing action: {action}")

    print(f"Next action to undo (peek): {history.peek()}")
    print("Undoing actions in LIFO order:")

    while not history.is_empty():
        print(f"Undo: {history.pop()}")

    print(f"Pop from empty stack: {history.pop()}")
    print(f"Peek at empty stack: {history.peek()}")

    single_stack = Stack()
    single_stack.push("One edit")
    print(f"Single-item stack empty before pop: {single_stack.is_empty()}")
    print(f"Removed item: {single_stack.pop()}")
    print(f"Single-item stack empty after pop: {single_stack.is_empty()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO: COFFEE SHOP CUSTOMERS ===")
    customers = Queue()

    for customer in [
        "Customer A",
        "Customer B",
        "Customer C",
        "Customer D"
    ]:
        customers.enqueue(customer)
        print(f"Joined the queue: {customer}")

    print(f"Next customer to be served (front): {customers.front()}")
    print("Serving customers in FIFO order:")

    while not customers.is_empty():
        print(f"Served: {customers.dequeue()}")

    print(f"Dequeue from empty queue: {customers.dequeue()}")
    print(f"Front of empty queue: {customers.front()}")

    single_queue = Queue()
    single_queue.enqueue("One customer")
    print(f"Single-item queue empty before dequeue: {single_queue.is_empty()}")
    print(f"Removed item: {single_queue.dequeue()}")
    print(f"Single-item queue empty after dequeue: {single_queue.is_empty()}")


if __name__ == "__main__":
    main()
