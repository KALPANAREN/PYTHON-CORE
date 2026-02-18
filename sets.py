s1 = {1, 2, 3}
s2 = set([1, 2, 3])
s3 = set("hello")   # {'h','e','l','o'}

# ONLY HASHABLE(IMMUTABLE) IS ACCEPTED
s = {1, "a", (1, 2), True}
s1 = {[1, 2], {3, 4}}  # TypeError

# updating
s.add(10)
s.update([4, 5, 6])

# removal
s.remove(3)   # Raises KeyError if missing
s.discard(3)  # No error if missing

#maths operations
a = {1, 2, 3}
b = {3, 4, 5}

a | b
a.union(b)
a & b
a.intersection(b)
a - b
a.difference(b)
a ^ b
a.symmetric_difference(b)

# comparisons
a = {1, 2}
b = {1, 2, 3}
a.issubset(b)     # True
b.issuperset(a)   # True
a <= b            # True
a < b   # Proper subset (not equal)

######### TRICKY QUESTIONS

S = {1, True, 0, False}
print(s) # {1, 0} since True==1 and False==0

# modification
for x in s:
    s.remove(x)  # ❌ RuntimeError

for x in s.copy():
    s.remove(x)  # correct way
