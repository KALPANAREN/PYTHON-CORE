# single element tuple
t = (10)     # ❌ int
t = (10,)    # ✅ tuple

# mutable objects inside tuple can change
t = (1, [2, 3])
t[1].append(4) 

print(t)  # (1, [2, 3, 4])

# packing and unpacking

t = 1, 2, 3
a, b, c = (1, 2, 3)
a, *b, c = (1, 2, 3, 4, 5) # extend unpacking
# a = 1, b = [2, 3, 4], c = 5

