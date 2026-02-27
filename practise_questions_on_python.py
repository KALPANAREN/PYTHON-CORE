def delete_dig_and_adj(s):
    if len(s)!=0:
        for i in range(1,len(s)):
            if s[i].isdigit() and not s[i-1].isdigit():
                s = s.replace(s[i],'')
                s = s.replace(s[i-1],'')
        print(s)
        return delete_dig_and_adj(s)
    else: 
        pass
         
delete_dig_and_adj('a23bc45def')

def delete_dig_and_adj(s):
    i = 1
    while i < len(s):
        if s[i].isdigit() and not s[i-1].isdigit():
            s = s[:i-1] + s[i+1:]  # Remove both characters
            i = max(1, i-1)  # Move index back to check for new pairs
        else:
            i += 1
    if len(s)==0:
        return 0
    else:
        delete_dig_and_adj(s)
a = delete_dig_and_adj('a23bc45def')
print(a)

word = "aaAbcBC"
d1 = {}
import pandas as pd
sa = pd.Series([1, 2, 3], index=list('abc'))   
print(sa) 

#group anagrams

s1 = ["eat","tea","tan","ate","nat","bat"]
s2 = {}
for str in s1:
    sorted_str = ''.join(sorted(str))
    if sorted_str not in s1:
        s2[sorted_str] = []
    else:
        s2[sorted_str].append(str)
print(s2)

# all occurences of substring in a list

    # using for loop

l1 = ["gfg is best", "gfg is good for CS",
             "gfg is recommended for CS"] 
l2 = ["is", "for"]
l3 = [ele1 for ele1 in l1 if all(ele2 in ele1 for ele2 in l2)]
print(l3)

    # using lambda

l3 = list(filter(lambda e1:all(e2 in e1 for e2 in l2),l1))
print(l3)

# sort list of strings by the len of string

list1 = ['intelligence', 'artificial', 'developer', "python","narendar","reddy"]
l2 = sorted(list1,key = lambda ele:len(ele))
print(l2)

#  sort list of strings by no of unique char in string

l1 = ['intelligence', 'artificial', 'developer', "python","narendar","reddy"]
l2 = sorted(l1,key=lambda ele:len(set(ele)))
print(l2)

# filter sublist if all elements in them are multiples of an input

    # using lambda

list1 = [[5, 10, 15], [4, 8, 3], [100, 15], [5, 10, 23]]
k = 5
l2 = list(filter(lambda ele1:all(ele2%k==0 for ele2 in ele1),list1))
print(l2)

    # using comprehension

list1 = [[5, 10, 15], [4, 8, 3], [100, 15], [5, 10, 23]]
k = 5
l2 = [ele for ele in list1 if all(ele2%k==0 for ele2 in ele)]
print(l2)

# extract strings with digit(s) in them
    #using lambda and filter

list1 = ['gf4g', 'is', 'best', '4', 'gee1ks']
l2 = list(filter(lambda ele:any(ch.isdigit() for ch in ele),list1))
print(l2)

    # using comp

list1 = ['gf4g', 'is', 'best', '4', 'gee1ks']
l2 = [ele for ele in list1 if any(ch.isdigit() for ch in ele)]
print(l2)

# get index of the subelement with a given string in it

    #using for loop

list1 = [["GFG", "best", "geeks"], ["geeks", "rock"],["GFG", "for", "CS"], ["Keep", "learning"]]
input = "GFG"
index = []
for idx,ele in enumerate(list1):
    if input in ele:
        index.append(idx)
print(index)

    # using comp

list1 = [["GFG", "best", "geeks"], ["geeks", "rock"],["GFG", "for", "CS"], ["Keep", "learning"]]
input = "GFG"
l2 = [idx for idx,ele in enumerate(list1) if input in ele]
print(l2)

# extract monodigit elements

    # using filter and lambda

list1 = [463, 888, 123, "aaa", 112, 111, "gfg", 939, 4, "ccc"]
l2 = list(filter(lambda ele:len(set(str(ele)))==1,list1))
print(l2)

    # comp

list1 = [463, 888, 123, "aaa", 112, 111, "gfg", 939, 4, "ccc"]
l2 = [ele for ele in list1 if len(set(str(ele)))==1]
print(l2)

# print subelements if all ele in them are greater than input

    # using lambda and filter

list1 = [[1, 1, 2, 3, 2, 3], [4, 4, 5, 6, 6], [1, 1, 1, 1], [4, 5, 6, 8]]
input = 3
l2 = list(filter(lambda ele:all(ele2>input for ele2 in ele),list1))
print(l2)

    # using comp

list1 = [[1, 1, 2, 3, 2, 3], [4, 4, 5, 6, 6], [1, 1, 1, 1], [4, 5, 6, 8]]
input = 3
l2 = [ele for ele in list1 if all(ele2>input for ele2 in ele)]
print(l2)

# count and say 

s1 = "3322255111"
d1 = {ch:s1.count(ch) for ch in s1}
l1 = ''.join([str(x)+str(y) for x,y in d1.items()])
print(l1) #o/p: 32235213

#longest substring without repeating characters
s = "abqwertyucdabcbbasdfgh"
s1 = []
s2 = ""
for i in range(len(s)):
    
    if s[i] not in s2:
        s2+=s[i]
    else:
        s2 = ""
        s2+=s[i]
    s1.append(s2)
long_sub_Str = sorted(s1,key=len,reverse=True)[0]
print(long_sub_Str)


#flattening nested list

    # using function

def flatten_nested_list(nested_list):
    flat_list = []
    for ele in nested_list:
        if isinstance(ele,list):
            flat_list.extend(flatten_nested_list(ele))
        else:
            flat_list.append(ele)
    return flat_list
result = flatten_nested_list([[1, 2, [3, 4]], [4, 5, 6], 10,11,[7, 8, 9]])
print(result)

    # using comprehension

nested_list = [[1, 2, [3, 4]], [4, 5, 6], 10,11,[7, 8, 9]]
sub_nest = [ele if isinstance(ele,list) else [ele] for ele in nested_list]
flat_list = [item for sub_list in sub_nest for item in sub_list]
print(flat_list) # works only for elements inside list without element again as sublist


# print 1-1/3+1/5-1/7 upto 1/15

l1 = []
for i  in range(3,16,4):
    s = '-'+'1'+'/'+str(i)
    l1.append(s)
    i+=2
    s = '+'+'1'+'/'+str(i)
    l1.append(s)
res = '1'+''.join(ele for ele in l1)
print(res)

# sort without sort function

l1 = [3,2,5,7,8,1,2]
for i in range(len(l1)):
    for j in range(len(l1)-i-1):
        if l1[j]>l1[j+1]:
            l1[j],l1[j+1] = l1[j+1],l1[j]
print(l1)

# print prime numbers in given range

n1 = int(input("enter the starting limit"))
n2 = int(input("enter the ending limit"))
for i in range(n1,n2):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

# operator overloading

class OperatorOverload():
    def __init__(self,m1,m2):
        self.sub1 = m1
        self.sub2 = m2
    
    def __add__(self,other):
        s1 = self.sub1+other.sub1
        s2 = self.sub2+other.sub2
        s3 = OperatorOverload(s1,s2)
        return s3

s1 = OperatorOverload(50,54)
s2 = OperatorOverload(78,98)
s3 = s1+s2
print(s3.sub1)


#roman number to integer

def romtoint(string:str) -> int: # type: ignore
    num = 0
    rom_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
    string = string.replace('IV','IIII').replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
    for ch in s:
        num+=rom_to_int[ch]
    return num
romtoint('IVXCIILX')

# integer to roman

def romtoint(num:int) -> str:
    rom = ""
    int_to_rom = {
            1: "I", 4: "IV",
            5: "V",   9: "IX",  
            10: "X",  40: "XL",
            50: "L",   90: "XC",
            100: "C",  400: "CD",
            500: "D",   900: "CM", 1000: "M"
        }
    for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
        while n<=num:
            rom+=int_to_rom[n]
            num-=n
    return rom
res = romtoint(976)
print(res)

# anagram words

s1 = "complement"
s2 = "compliment"
d1 = {ch:s1.count(ch) for ch in s1}
d2 = {ch:s2.count(ch) for ch in s2}
if d1==d2:
    print("anagrams")
else:
    print("non anagrams")