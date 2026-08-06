stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

print(stack) # [10, 20, 30]

# Peek
print(stack[-1]) # 30

# Pop
print(stack.pop()) # 30

print(stack)  # [10, 20]

# Size
print(len(stack)) # 2

# Empty?
print(len(stack) == 0) # False

# PRODUCTION GRADE STACK

class Stack:
    """LIFO stack implementation using Python list."""

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def clear(self):
        self._items.clear()

    def __len__(self):
        return len(self._items)

    def __bool__(self):
        return bool(self._items)

    def __repr__(self):
        return f"Stack({self._items})"

s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s) # Stack([10, 20, 30])
print(s.peek()) # 30
print(s.pop()) # 30
print(s)    # Stack([10, 20])