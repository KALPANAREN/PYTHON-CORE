l1 = [1,3,4]
l2 = [7,9,12]

##### COPY #####

l3 = l1
l1.insert(10,56)
print(l1)   # [1, 3, 4, 56]
print(l3)   # [1, 3, 4, 56]

######## SHALLOW COPY ########

l4 = [[1,3,4],[7,9,12]]
l5 = l4.copy()

#changes in main list

l4.append(267)
print(l4)   # [[1, 3, 4], [7, 9, 12], 267]
print(l5)   # [[1, 3, 4], [7, 9, 12]]

# changes in sublists

l4[1].insert(3,545) 
print(l4)   # [[1, 3, 4], [7, 9, 12, 545], 267]
print(l5)   # [[1, 3, 4], [7, 9, 12, 545]]

########## DEEP COPY
l6 = [[1, 3, 4], [7, 9, 12, 545]]
from copy import deepcopy
l7 = deepcopy(l6)

#change in main list

l6.extend([87,45])
print(l6)   # [[1, 3, 4], [7, 9, 12, 545], 87, 45]
print(l7)   # [[1, 3, 4], [7, 9, 12, 545]]

# change in sublists

l6[1].pop()
print(l6)   # [[1, 3, 4], [7, 9, 12], 87, 45] 
print(l7)   # [[1, 3, 4], [7, 9, 12, 545]]