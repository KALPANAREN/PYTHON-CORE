# pass by value(means passing immutables)

x = 2000
print(id(x))
def pass_by_value(x):
    x = x+46588
    print(x)
    print(id(x))
pass_by_value(x)
print(x)

# pass by reference( means passing mutables)

l1 = [2,3,4,5]
def pass_by_ref(l1):
    l1.append(234)
    print(l1)
pass_by_ref(l1)
print(l1)