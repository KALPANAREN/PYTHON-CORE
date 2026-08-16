from collections import deque
from typing import Deque, Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    """
    A FIFO queue implemented using collections.deque.
    """

    def __init__(self) -> None:
        self._items: Deque[T] = deque()

    def enqueue(self, item: T) -> None:
        """Add an item to the rear of the queue."""
        self._items.append(item)

    def dequeue(self) -> T:
        """Remove and return the front item."""
        if not self._items:
            raise IndexError("dequeue from empty queue")

        return self._items.popleft()

    def front(self) -> T:
        """Return the front item without removing it."""
        if not self._items:
            raise IndexError("queue is empty")

        return self._items[0]

    def clear(self) -> None:
        """Remove all items."""
        self._items.clear()

    def __len__(self) -> int:
        return len(self._items)

    def __bool__(self) -> bool:
        return bool(self._items)

    def __repr__(self) -> str:
        return f"Queue({list(self._items)})"

q = Queue()

q.enqueue("Alice")
q.enqueue("Bob")
q.enqueue("Charlie")

print(q)    #   Queue(['Alice', 'Bob', 'Charlie'])

print(q.front()) #Alice

print(q.dequeue())   # Alice

print(q)    #   Queue(['Bob', 'Charlie'])

print(len(q))   # 2

print(bool(q))  # True