l1 = [1,2,4,5,7]
print(dir(l1))
i1 = iter(l1)
print(dir(i1))

class MyIterator():
    def __init__(self,start,finish):
        self.begin =  start
        self.end = finish
    def __iter__(self):
        return self
    def __next__(self):
        if self.begin>self.end:
            raise StopIteration
        current = self.begin
        self.begin+=1
        return current

m1 = MyIterator(4,10)
for m in m1:
    print(m)


# generator

def gen_func(n):
    for  i in range(n):
        yield i
    
x = list(gen_func(8))
print(x)