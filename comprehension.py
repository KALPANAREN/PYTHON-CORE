"""
Always read the nested comprehensions from left to right.
The first for loop is the outermost loop.
The last if (at the very end) is a filter.
The if-else at the very beginning is part of the expression (the result).
"""

# IF - ELSE CONDITION

evens = [x for x in range(10) if x % 2 == 0] # if is placed at end of the loop
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)] # if-else is placed at start of the loop

# NESTED LIST COMP
"""
Nested comprehensions are read in the same order 
as they would be written in a standard for loop (top to bottom)
"""
matrix = [[1, 2], [3, 4], [5, 6]]

# The Logic:
# for row in matrix:
#     for num in row:
#         flattened.append(num)

flattened = [num for row in matrix for num in row]

# NESTED CONSTRUCTION

# Create a 3x3 identity matrix
matrix = [[1 if row == col else 0 for col in range(3)] for row in range(3)]

# NESTED COMPREHENSION WITH IF FILTERING

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Order: Outer Loop -> Inner Loop -> Filter
filtered = [num for row in matrix for num in row if num % 2 == 0]

# NESTED COMPREHENSION WITH IF-ELSE FILTERING

matrix = [[1, 2, 3], [4, 5, 6]]
processed = ["Even" if num % 2 == 0 else "Odd" for row in matrix for num in row]

# NESTING, FILTERING, IF-ELSE
"""
syntax: [Transform (if-else) | Outer Loop | Inner Loop | Filter (if)]
"""
matrix = [[1, 2, 3], [4, 5, 6]]

result = [num**2 if num % 2 == 0 else num**3 for row in matrix for num in row if num > 2]

# Breakdown:
# 1. for row in matrix -> for num in row (Flattening)
# 2. if num > 2 (Filtering out 1 and 2)
# 3. 3**3, 4**2, 5**3, 6**2 (Transforming 3, 4, 5, 6)
# Output: [27, 16, 125, 36]

# PRACTISE QUESTIONS

"""
nums = range(-10, 11)
Create a list where:
negative numbers are discarded
even numbers are squared
odd numbers are cubed
"""
nums = range(-10, 11)
pos_even_odd = [num**2 if num%2==0 else num**3 for num in nums if num > 0]

"""Create a flat list of:
absolute values
only for numbers divisible by 3"""

matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
l = [abs(ele) for sub in matrix for ele in sub if abs(ele)%3==0]

"""Create a list where:

replace with "short" if word shorter than 4 chars
words 4–6 chars → uppercase
words longer than 6 chars → reversed string"""

words = ["apple", "hi", "banana", "cat", "elephant"]
new = ["short" if len(word)<4 else word.upper() if 4<len(word)<=6 else word[::-1] for word in words]

"""
remove duplicates
preserve order
no set() directly
single list comprehension
"""
items = ["a", "b", "a", "c", "b", "d"]
uniques = [items[i] for i in range(len(items)) if items[i] not in items[:i]]

# print only error above 400

text = "Error:404, Success:200, Redirect:301, Error:500"
t = text.split(',')
d1 = [ele.split(':')[1] for ele in t if ele.startswith("Error") and int(ele.split(':')[1])>400]
d2 = [int(ele.split(':')[1]) 
 for ele in text.split(',') 
 if ele.startswith("Error") and int(ele.split(':')[1]) > 400]
print(d2)

#flatten only for odd number and  multiply by 10

nested = [[[1, 2], [3]], [[4, 5]], [[6], [7, 8]]]
flatten = [e*10 for subnest in nested for ele in subnest for e in ele if e%2!=0]
print(flatten)

# write comprehension for the following loop code
result = []
matrix = [[1,3],[2,4,5]]
for row in matrix:
    for x in row:
        if x > 0 and x % 2 == 0:
            result.append(x ** 2)

result = [x**2 for row in matrix for x in row if x > 0 and x % 2 == 0] # ANSWER