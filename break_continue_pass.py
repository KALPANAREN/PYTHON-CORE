for i in range(10):
    if i==5:
        break
    print(i) # 0,1,2,3,4

for i in range(10):
    if i==5:
        continue
    print(i) # 0,1,2,3,4,6,7,8,9

for i in range(10):
    if i==5:
        pass
    print(i) # 0,1,2,3,4,5,6,7,8,9