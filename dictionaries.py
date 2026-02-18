# creating an empty dict
empty_dict = dict()
print(empty_dict)

empty_dict1 = {}
print(empty_dict1)

emp = {"name":"Naren","age":32,"band":"TE02","name":"Kalpa"}
print(emp) #{'name': 'Kalpa', 'age': 32, 'band': 'TE02'} # though we defined duplicate key it's removed in the output
print(emp.get('name'))
print(emp.get("salary")) #None
print(emp.get("salary",100000)) #100000
emp["location"] ="India"
print(emp) #{'name': 'Kalpa', 'age': 32, 'band': 'TE02', 'location': 'India'}

keys = emp.keys() #dict_keys(['name', 'age', 'band', 'location'])
values = emp.values() #dict_values(['Kalpa', 32, 'TE02', 'India'])
items = emp.items() # dict_items([('name', 'Kalpa'), ('age', 32), ('band', 'TE02'), ('location', 'India')])


# copy
emp1 = emp
emp["name"] = "Narendar"
print(emp,emp1) # both are same since memory is same

# shallow copy
emp1 = emp.copy()
emp1["name"] = "suryaprakash"
print(emp1,emp) # different since memory is different

# iteration through dictionary

for key in emp.keys():
    print(key)
for value in emp.values():
    print(value)
for key,value in emp.items():
    print(f"{key}:{value}")

#iteration through nested dictionary

nested_dict = {"Narendar":{"age":32,"tech":"python","company":"GL"},
               "Niranjan":{"age":34,"tech":"Angular","company":"Dell"}}

for name,data in nested_dict.items():
    print(f"{name}:{data}")
    for key,value in data.items():
        print(f"{key}:{value}")

    
# merge two dictionaries
merge_dict = {**emp,**nested_dict}
print(merge_dict)

# common ways to create dictionary
d1 = {}                          # empty dict
d2 = dict()                      # empty dict
d3 = {"a": 1, "b": 2}
d4 = dict(a=1, b=2)
d5 = dict([("a", 1), ("b", 2)])

# valid keys
d = {
    1: "int",
    3.14: "float",
    "key": "string",
    (1, 2): "tuple"
}

# invalid keys
d = {[1, 2]: "list"}    # TypeError since keys should be immutable but we mentioned a list here so error
d = {{1: 2}: "dict"}   # TypeError

# tricky area
d = {(1, 2): "ok"}      # Works
d = {([1, 2]): "no"}   # Error

#update
d.update({"c": 3, "d": 4})

# removing element
d = {"a": 1, "b": 2, "c": 3}

d.pop("a")          # removes 'a'
d.popitem()         # removes LAST inserted item
del d["b"]          # deletes key
d.clear()           # empties dictionary

d.pop("x")          # KeyError
d.pop("x", 0)       # Safe, returns 0


# EXCERSICE

# print emma's marks
students = {
    "s1": {"name": "John", "marks": 85},
    "s2": {"name": "Emma", "marks": 92}
}

for student in students:
    if students[student]["name"]=="Emma":
        print(students[student]["marks"])

# change the dictionary as per marks order
marks = {"John": 85, "Emma": 92, "Ryan": 78}
desc_marks = sorted(marks.values(),reverse=True)
new_dict = {}
for mark in desc_marks:
    for key in marks.keys():
        new_dict[mark]=key
print(new_dict)              # {92: 'Ryan', 85: 'Ryan', 78: 'Ryan'}


# Group Words by Length

words = ["apple", "bat", "car", "elephant", "dog", "ant"]
output = {3: ['bat', 'car', 'dog', 'ant'], 5: ['apple'], 8: ['elephant']}

lengths = sorted(set([len(word) for word in words]))
output = {length:list() for length in lengths} # length:[] is also fine

for length in output:
    for word in words:
        if len(word)==length:
                output[length].append(word)
print(output)

# group words by first character

words = ["apple", "ant", "banana", "bat", "cat", "car"]
output = {word[0]:list() for word in words}
for key in output:
    for word in words:
        if word.startswith(key):
            output[key].append(word)
print(output)

# group words by vowels and consonants in them

words = ["apple", "english", "myth", "rhythm", "cat", "car","crypt"]
output = {"vowels":list(), "consts":list()}

exp = [output["vowels"].append(word) if any(ch in "aeiou" for ch in word) else
       output["consts"].append(word) for word in words] 
print(output)

# Build a Student Report System

data = [
    ("John", "Math", 85),
    ("John", "Science", 90),
    ("Emma", "Math", 95),
    ("Emma", "Science", 88)
]

# output = {
#   "John": {"Math": 85, "Science": 90},
#   "Emma": {"Math": 95, "Science": 88}
# }

stds = set([data[i][0] for i in range(len(data))])
output = {std:{} for std in stds}
for std in output:
    for ele in data:
        if ele[0]==std:
            output[std][ele[1]]=ele[2]
print(output)

# Invert a Dictionary with Duplicate Values

data = {"a": 1,"b": 2,"c": 1,"d": 2,"e": 3}
values = set([data[key] for key in data])
output = {value:list() for value in values}
for value in values:
    for key in data.keys():
        if data[key]==value:
            output[value].append(key)

print(output)   # {1: ['a', 'c'], 2: ['b', 'd'], 3: ['e']}

# Find Top Scorer from Nested Dictionary

students = {
    "John": {"Math": 85, "Science": 90},
    "Emma": {"Math": 95, "Science": 88},
    "Ryan": {"Math": 80, "Science": 70}
}
output = {student:sum(students.get(student).values()) for student in students}
print(output)

#
sales = [
    ("apple", 10),
    ("banana", 5),
    ("apple", 7),
    ("banana", 3),
    ("mango", 8)
]
fruits = {fruit[0]:list() for fruit in sales}

for fruit in fruits:
    for fruit_info in sales:
        if fruit==fruit_info[0]:
            fruits[fruit].append(fruit_info[1])

# what are the courses the students are enrolled in???

students = {
    101: "Alice",102: "Bob",103: "Charlie"
}
student_courses = {
    101: ["CS101", "MA101"],102: ["CS101"],103: ["MA101", "PH101"]
}
courses = {
    "CS101": "Computer Science","MA101": "Mathematics","PH101": "Physics"
}

keys = list(students.values())
values = list(student_courses.values())
name_courses = {x:y for x,y in zip(keys,values)} # {'Alice': ['CS101', 'MA101'], 'Bob': ['CS101'], 'Charlie': ['MA101', 'PH101']}
for student in name_courses:
    name_courses[student] = [courses.get(code,"unknown course") for code in name_courses[student]]
for student, course_list in name_courses.items():
    print(f"{student}:{','.join(course_list)}")
