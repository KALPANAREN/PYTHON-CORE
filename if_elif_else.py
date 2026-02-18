# if else

age = 20

if age>18:
    print("allowed to vote")

else:
    print("need to wait")

# multiple if's
n = 20
if n<25:
    print("n is less than 25")

if n<30:
    print("n is less than 30")

#if and mutiple elif's

n = 10

if n<5:
    print("n is less than 5")

elif n<20:
    print("n is less than 20")

elif n<25:
    print(" n is less than 25")

#if,elif and else

n = 25

if n<20:
    print("n is less than 20")

elif n<30:
    print("n is less than 30")

else:
    print("will be print only if and elif fails")

# practical example- leap year

year = 2506
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is leap year")
        else:
            print(year,"is not leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")

