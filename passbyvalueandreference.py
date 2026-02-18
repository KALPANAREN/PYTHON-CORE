# pass by value

x = 20
def pass_by_value(x):
    x = x+46
    print(x)
pass_by_value(x)
print(x)

# pass by reference

l1 = [2,3,4,5]
def pass_by_ref(l1):
    l1.append(234)
    print(l1)
pass_by_ref(l1)
print(l1)