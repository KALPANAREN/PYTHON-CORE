for i in range(5):
    print(i)

for i in range(1,5):
    print(i)

for i in range(1,20,2):
    print(i)

for i in range(20,2,-3):
    print(i)

# find sum of first 10 natural numbers using while loop

n = 10
sum = 0
count = 1
while count<=n:
    sum+=count
    count+=1
print(sum)

# using for loop
n = 10
sum = 0
for i in range(n):
    sum+=i
print(sum)