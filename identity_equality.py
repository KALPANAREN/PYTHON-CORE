a = [1,2]
b = [1,2] # a and b are assigned to two different objects
print(id(a))
print(id(b))
if a==b:
    print(True)
if a is b:
    print(True)

a = [3,4]
b = a # both are assigned to same object


# REBINDING

l1 = [1,2,5]
print(id(l1))
l1 = l1+[7,8] # mutation affects all references and rebinding affects one reference
print(id(l1))