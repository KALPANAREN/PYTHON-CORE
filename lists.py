nums = [1, 2, 3]

# Adding elements
nums.append(4)              # [1, 2, 3, 4]
nums.extend([5, 6])         # [1, 2, 3, 4, 5, 6]
nums.insert(1, [10,24])          # [1, [10,24], 2, 3, 4, 5, 6]

# Removing elements
nums.remove(10)             # removes first occurrence of 10
last = nums.pop()           # removes last element from the list
nums.pop(0)                 # removes element at index 0
nums.clear()                # []

# Searching
nums.index(4)               # gives the position of number 4 
nums.count(1)               # gives the count of 1 in list

# Sorting & reversing
nums.sort()                 # in-place sort
nums.reverse()              # in-place reverse

fruits = [
    "Apple", "Banana", "Orange", "Mango", "Pineapple",
    "Grapes", "Strawberry", "Blueberry", "Watermelon", "Papaya",
    "Kiwi", "Cherry", "Peach", "Pear", "Plum",
    "Guava", "Pomegranate", "Lychee", "Fig", "Coconut"
]
"""
step should always be positive number
list[start : stop : step]
Positive step (+1) → move left to right. Therefore, start should be before stop.
Negative step (-1) → move right to left. Therefore, start should be after stop.
fruits = [
    "Apple",       #  0   -20
    "Banana",      #  1   -19
    "Orange",      #  2   -18
    "Mango",       #  3   -17
    "Pineapple",   #  4   -16
    "Grapes",      #  5   -15
    "Strawberry",  #  6   -14
    "Blueberry",   #  7   -13
    "Watermelon",  #  8   -12
    "Papaya",      #  9   -11
    "Kiwi",        # 10   -10
    "Cherry",      # 11   -9
    "Peach",       # 12   -8
    "Pear",        # 13   -7
    "Plum",        # 14   -6
    "Guava",       # 15   -5
    "Pomegranate", # 16   -4
    "Lychee",      # 17   -3
    "Fig",         # 18   -2
    "Coconut"      # 19   -1
]
"""
print(fruits[2:10]) #['Orange', 'Mango', 'Pineapple', 'Grapes', 'Strawberry', 'Blueberry', 'Watermelon', 'Papaya']
print(fruits[2:-7]) #['Orange', 'Mango', 'Pineapple', 'Grapes', 'Strawberry', 'Blueberry', 'Watermelon', 'Papaya', 'Kiwi', 'Cherry', 'Peach']
print(fruits[-7:-4]) #['Pear', 'Plum', 'Guava']
print(fruits[-2:-7]) # answers is []
print(fruits[-10:-4:2]) #['Pear', 'Plum', 'Guava']

fruits1 = ["apple"]
fruits1[2:] =  "Watermelon"
print(fruits1) #['apple', 'W', 'a', 't', 'e', 'r', 'm', 'e', 'l', 'o', 'n']

# Initialization
fruits = ['apple', 'banana', 'cherry']

# 1. Adding elements
fruits.append('orange')          # Adds to the end: ['apple', 'banana', 'cherry', 'orange']
fruits.insert(1, 'blueberry')    # Inserts at index 1: ['apple', 'blueberry', 'banana', 'cherry', 'orange']

# 2. Removing elements
fruits.remove('banana')          # Removes by value
popped_item = fruits.pop(0)      # Removes by index and returns it ('apple')

# 3. Finding and Ordering
index_of_cherry = fruits.index('cherry')
fruits.sort(reverse=True)        # Sorts in-place (alphabetical descending)

mixed = [1, "Hello", 3.14, True]

###### CONFUSING TOPICS ########

# REMOVING ITEMS WHILE ITERATING

nums = [1, 2, 4, 4]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
"""
this doesn't work since after removal of 2, the first 4 shifts 
to index 1 whose iteration whose iteration is already done """
print(nums)   # [1, 4] ❌
 
nums = [n for n in nums if n % 2 != 0] # CORRECT WAY

nums = [1, 2, 3, 4] # ANOTHER CORRECT WAY
for n in nums[:]:
    if n % 2 == 0:
        nums.remove(n) 

# SLICING CREATES A shallow copy

a = [1, 2, 3, 4]
b = a[:] # shallow copy is created
b.append(5)
print(a)   # [1, 2, 3, 4] ✔️

# TRUTH VALUE OF LISTS

if []:
    print("won't run")
if [1]:
    print("will run")

# += vs +

a = [1, 2]
b = a

a += [3]
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]  

a = [1, 2]
b = a

a = a + [3]
print(a)  # [1, 2, 3]
print(b)  # [1, 2]     

# SLICE ARRANGEMENT
a = [1, 2, 3, 4]
a[1:3] = [9, 9, 9]

print(a)  # [1, 9, 9, 9, 4]

# EMPTY SLICE vs INDEX

a = [1, 2, 3]

print(a[5:10])  # []
print(a[5])     # ❌ IndexError

# PRACTISE QUESTIONS

#########   flatten a list  ########## 

# using ininstance and yield

nest = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item
x = list(flatten(lst=nest))
print(x)

# using recursive comprehension

nest = [1, [2, 3, [4, 5]], 6, [7, [8, 9]]]
def flat_comp(lst):
    return [ele for item in lst for ele in (flat_comp(item) if isinstance(item,list) else [item])]
x = flat_comp(nest)
print(x)

# Keep sentences that start has all keywords in another list
sentences = [
    "python is easy",
    "python is powerful",
    "java is powerful",
    "python and java"
]

keywords = ["python", "powerful"]

lines = [line for line in sentences if all(word in line for word in keywords)]
print(lines)

# # Keep names that start with any prefix in another list
names = ["Naren", "Neha", "Ravi", "Raj", "Nikhil"]
prefixes = ["Na", "Ra"]

res = [name for name in names if any(prefix in name for prefix in prefixes)]
print(res)

# find sentences in list 1 those have only one word from l2, not both
l1 = [
    "python is powerful",
    "java is fast",
    "python and java",
    "c++ is efficient",
    "python is easy"
]

l2 = ["python", "java"]

l3 = [sentence for sentence in l1 if sum(word in sentence for word in l2 )==1]

######### FILTER + LAMBDA

# keep users Have "Python" in skills AND Have experience ≥ 3 AND are active
users = [
    {"name": "Naren", "skills": ["Python", "FastAPI"], "exp": 4, "active": True},
    {"name": "Ravi", "skills": ["Java"], "exp": 5, "active": True},
    {"name": "Neha", "skills": ["Python", "Django"], "exp": 2, "active": True},
    {"name": "Kiran", "skills": ["Python"], "exp": 3, "active": False},
]

res = list(filter(lambda user:"Python" in user['skills'] and user['exp']>=3 and user['active']==True,users))
print(res)
# filter sentences with only one word from keywords

sentences = ["python is powerful","java is fast","python and java","c++ is efficient"]
keywords = ["python", "java"]
res = list(filter(lambda sent:sum(keyword in sent for keyword in keywords)==1,sentences))
print(res)

# filter sublist where Sum of elements > 20 AND at least one even number exists

data = [
    [2, 4, 6],
    [5, 7, 9],
    [10, 5, 8],
    [1, 2, 3, 4, 20]
]

res = list(filter(lambda lst:sum(lst)>20 and any(num%2==0 for num in lst),data))
print(res)

# condition based filtering
conditions = {
    "min_exp": 3,
    "required_skill": "Python"
}

employees = [
    {"name": "A", "exp": 2, "skills": ["Python"]},
    {"name": "B", "exp": 4, "skills": ["Java"]},
    {"name": "C", "exp": 5, "skills": ["Python", "Django"]},
]

result = list(filter(lambda e: e["exp"] >= conditions["min_exp"] and conditions["required_skill"] in e["skills"], employees ))
print(result)

# multilevel dictionary filtering

products = [
    {"name": "Laptop", "price": 45000, "rating": 4.5, "category": "electronics"},
    {"name": "Phone", "price": 15000, "rating": 4.2, "category": "electronics"},
    {"name": "Headphones", "price": 2000, "rating": 3.8, "category": "electronics"},
    {"name": "Chair", "price": 3000, "rating": 4.5, "category": "furniture"},
]

result = list(filter(
    lambda p: p["price"] < 5000
              and p["rating"] >= 4
              and p["category"] == "electronics",
    products
))

print(result)

# PRINT THE NUMBERS WHOSE DIGIT SUM IS PRIME

def prime(n):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        return n

nums = [14, 23, 29, 31, 44, 57, 82]
prime_sum_nums = list(filter(lambda num:prime(sum(int(ch) for ch in str(num))),nums))
print(prime_sum_nums)

# for best logic, replace the prime logic as below
def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
    
# FIND THE WORDS THAT HAS ONLY TWO VOWELS

words = ["table", "sky", "education", "python", "moon", "rhythm", "applee", "apple"]

def two_vowel(word):
    return sum(ch in 'aeiou' for ch in word.lower())==2

two_vowel_words = list(filter(lambda word:two_vowel(word),words)) 
print(two_vowel_words)

# FIND THE WORDS THAT HAS ONLY TWO VOWELS WHERE THE VOWELS ARE NOT ADJACENT

words = ["table", "sky", "education", "python", "moon", "rhythm"]

def two_vowels_not_adjacent(word):
    word = word.lower()
    vowels = "aeiou"
    positions = [i for i, ch in enumerate(word) if ch in vowels]
    return len(positions) == 2 and positions[1] - positions[0] > 1

result = list(filter(lambda w: two_vowels_not_adjacent(w), words))
print(result)

# KEEP LISTS WHOSE MAX APPEARS ONLY ONCE

data = [
    [1, 3, 5, 5],
    [2, 9, 4, 1],
    [7, 7, 7],
    [10, 2, 8]
]

def max_once(l1):
    s1 = sorted(l1,reverse=True)
    return  s1[1]!=s1[0]
data1 = list(filter(lambda list1:max_once(list1),data))
print(data1)

# better code
"""
the above max_once function won't work for empty list and single element lists
"""

def max_once(lst):
    m = max(lst)
    return lst.count(m) == 1

# KEEP NUMBERS THAT ARE NOT DIVISIBLE BY ANY DIGIT THEY CONTAIN

nums = [12, 13, 22, 37, 48, 101]
def div_digits(num):
    if "1" in str(num):
        return False
    digs = [int(ch) for ch in str(num) if int(ch)!=0]
    l1 = [True for dig in digs if num%dig!=0]
    return len(l1)==len(digs)
ans = list(filter(lambda num:div_digits(num),nums))
print(ans)

# best logic
def div_digits(num):
    digits = [int(ch) for ch in str(num) if ch != '0']
    return all(num % d != 0 for d in digits)

# KEEP PALINDROMES THAT ARE DIVISIBLE BY k

nums = [121, 131, 141, 151, 171, 181, 191,235]

def pal_divisible(num, k):
    s = str(num)
    return s == s[::-1] and num % k == 0

pal3 = list(filter(lambda n: pal_divisible(n, 3), nums))
