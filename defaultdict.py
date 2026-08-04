employees = [
    ("Alice", "HR"),
    ("Bob", "IT"),
    ("Charlie", "HR"),
    ("David", "IT"),
    ("Eva", "Finance"),
]

# traditional approach
groups = {}
for name,dept in employees:
    if dept not in groups:
        groups[dept] = []
    groups[dept].append(name)

# defaultdict

from collections import defaultdict
groups = defaultdict(list)
for name, dept in employees:
    groups[dept].append(name)

"""
suppose we ask for a key that is not present?
with defaultdict, it returns empty by default without raising key error
because the list(not list()) we are passing automatically creates an empty if that key was not present in the dictionary"""
print(groups["python"]) # []

# another example defaultdict(list)

d = defaultdict(list)
d["A"].append(1)
d["A"].append(2)
print(d)    # {'A':[1,2]}

#   defaultdict(float)

scores = defaultdict(float)
scores["Alice"] += 2.5
print(scores)

#   defaultdict(set)
friends = defaultdict(set)
friends["Alice"].add("Bob")
friends["Alice"].add("Charlie")
friends["Alice"].add("Bob")
print(friends)  #   {'Alice':{'Bob','Charlie'}}

#   Custom Default Factory
from collections import defaultdict
d = defaultdict(lambda: "Unknown")
print(d["City"])    #   {'City':'Unknown'}


#   what is the diffence between dict() and defaultdict()?
"""
dict.get() returns None but it doesn't create key with empty assigned whereas a defaultdict does this"""
d = {}
print(d.get("A", [])) # []
print(d) # {}

d = defaultdict(list)
print(d["A"]) # {'A':[]}
