from collections import Counter
nums = [1, 2, 2, 3, 3, 3]
print(Counter(nums))
print(Counter("mississippi"))

c = Counter([1, 1, 2])
print(c[1])
print(c[3])

c = Counter()
c["A"] += 2
c["B"] += 1
print(c)

# most common

"""
Sorting inside most_common()
O(k log k) where k = unique elements"""
from collections import Counter
nums = [10,20,10,30,20,10]
c = Counter(nums)
print(c.most_common())
print(c.most_common(1))

# elements

from collections import Counter
c = Counter({
    "A":3,
    "B":2,
    "C":1
})
print(list(c.elements())) # ['A','A','A','B','B','C']

# update

from collections import Counter
c = Counter("apple") # {'a':1,'p':2,'l':1,'e':1}
c.update("apple") # {'a':2,'p':4,'l':2,'e':2}

c = Counter([1,2,2]) # {1:1,2:2}
c.update([2,3])     # {1:1,2:3,3:1}

#   subtract()
from collections import Counter
c = Counter([1,1,2,3])
c.subtract([1,3]) # {1:1,2:1,3:0}

c = Counter([1])
c.subtract([1,1])   # Counter({1:-1})

#   Counter Arithmetic
from collections import Counter
c1 = Counter(a=2,b=1)
c2 = Counter(a=1,b=3)

print(c1+c2)    # Counter({'a':3,'b':4})

#   Subtraction
print(c1-c2)    #   Counter({'a':1})