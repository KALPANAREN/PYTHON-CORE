from collections import deque
"""everything works similar to lists"""
# empty deque
d = deque()

# converting list to deque

d = deque([10,20,30])

# creating from an iterable
d = deque((1,2,3))
d = deque("Python")
d = deque(i*i for i in range(5))

# converting back to list

d = deque([10,20,30])
nums = list(d)

# length
print(len(d))

# membership
print(20 in d)

# indexing

d = deque([10,20,30,40])
print(d[2]) # 30

# assignment
d = deque([10,20,30])
d[1] = 999
print(d)


# append()

d = deque([10, 20, 30])
d.append(40)
print(d)    #deque([10, 20, 30, 40])

#appendleft()
d = deque([10,20,30])
d.appendleft(5)
print(d)    #deque([5,10,20,30])

#pop()
d = deque([10,20,30])
x = d.pop()
print(d)    #deque([10,20])

#popleft()
d = deque([10,20,30])
x = d.popleft()
print(d)    #deque([20,30])

# empty deque raises index error if we try to remove elements

#   QUEUE USES append() AND popleft(). STACK USES append() and pop()

# rotate()
d = deque([10, 20, 30, 40])
d.rotate(1) #deque([40, 10, 20, 30])

d = deque([10,20,30,40])
d.rotate(2) #deque([30,40,10,20])

d = deque([10, 20, 30, 40])
d.rotate(-2)    #[30 40 10 20]

"""use cases are round robin scheduling:
Task A
Task B
Task C

↓

After one rotation

Task B
Task C
Task A

Multiplayer Games:
Player A
↓
Player B
↓
Player C
Circular Buffer:
Instead of moving every element, rotate the deque.

Load Balancing:
Server1
Server2
Server3
Rotate servers after each request.
"""

# maxlen
"""
A deque can have a fixed maximum size

"""
from collections import deque

d = deque(maxlen=3)
d.append(10)
d.append(20)
d.append(30)
print(d) # deque([10,20,30], maxlen=3)

d.append(40)
print(d) # deque([20,30,40], maxlen=3)

d = deque([10,20,30], maxlen=3)
d.appendleft(5)
print(d)    # deque([5,10,20], maxlen=3)
"""use case of maxlen are
1)  recent search history ex: last 10 search
2) browser history
3) log buffer

Sliding Window:

Very common in Machine Learning, Signal Processing, Time Series and Streaming Analytics

Example:

window = deque(maxlen=5)

As new values arrive, old values automatically disappear."""
