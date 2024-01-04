"""
Iterator is an object inside the loop which fetch the element one by one.
2.It keeps only one item in the memory and wisely use the memory.
3.Iterable is an object on which we can run loop
4.Iterale give us an iterator
4.Every iterator is an iterable
5.But Every iterable is not an iterator
6.There are 2 methods to check this object is iterable or not
7.FIrst run a for loop on that object and 2nd dir(obj)-->if __iter__ is present than
it is iterable otherwise not.
8.Eaach iter

"""
"""
import sys
list1 = [x for x in range(1,1000)]
# for _ in list1:
#     print(_*2)
print(sys.getsizeof(list1))#-->bits
print(sys.getsizeof(list1)/8)#-->bits

xrange = range(1,1000)
print(sys.getsizeof(xrange))

list2 = [1,2,3,4]
print(type(list2))

x = iter(list2)
print(type(x))

list3 = [1,2,3,4]
iter_list3 = iter(list3)
print(iter_list3)
print(dir(iter_list3))

print(next(iter_list3))
print(next(iter_list3))
print(next(iter_list3))
print(next(iter_list3))
# print(next(iter_list3))#it will give an error for stop iteration

def my_own_for_loop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break
l1 = [1,2,3,4,5,6]
range_val = range(0,11)
touple1 = (1,2,3,4,5,6,7)
mydict = {0:1,1:1,2:2,3:6}
my_own_for_loop(l1)
print("-"*15)
my_own_for_loop(range_val)
print("-"*15)
my_own_for_loop(touple1)
print("-"*15)
my_own_for_loop(mydict)
print("-"*15)
"""

#Create own range function
"""
num = [1,2,3,4,5]
iter_obj = (iter(num))
iter_obj2 =(iter(iter_obj))
print(iter_obj,"\t",iter_obj2)

print(id(iter_obj))
print(id(iter_obj2))
"""

"""class MyOwnRange:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __iter__(self):
        return MyOwnRangeIterator(self)
class MyOwnRangeIterator:
    def __init__(self,iterable_obj):
        self.iterable = iterable_obj
    def __iter__(self):
        return self
    def __next__(self):
        if self.iterable.start >=self.iterable.end:
            raise StopIteration
        else:
            current = self.iterable.start
            self.iterable.start+=1
            return current

# for i in MyOwnRange(0,11):
#     print(i)

def gen_func():
    yield "This is the 1st statement"
    yield "This is the 2nd statement"
    yield "This is the 3rd statement"
gen = gen_func()
for i in gen:
    print(i)
    
"""
"""
class MyOwnRange:

    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __iter__(self):
        return MyOwnRangeIterator(self)
class MyOwnRangeIterator:
    def __init__(self,iterable_obj):
        self.iterable =iterable_obj
    def __iter__(self):
        return self
    def __next__(self):
        if self.iterable.start >=self.iterable.end:
            raise StopIteration
        else:
            current = self.iterable.start
            self.iterable.start +=1
            return current

for _ in MyOwnRange(0,20):
    print(_)
"""
"""
import sys
L = [x**2 for x in range(1000000)]
print(sys.getsizeof(L))

l_range = range(10000000)
print(sys.getsizeof(l_range))


def generator():
    yield "This is the 1st statement"
    yield "This is the 2nd statement"
    yield "This is the 3rd statement"
gen = generator()
# print(type(gen))
# print(next(gen))
# print(next(gen))
print(next(gen))
print("-----------------")
for i in gen:
    print(i)

# Difference between yield and return
# return statement does its work in once and move out of the memory
#yield -->remember the work done last time and done work partially.

def square(num):
    for i in range(1,num+1):
        yield i**2
gen = square(10)
print(next(gen))
print(next(gen))

for i in gen:
    print(i)

def my_gen_range(start,end):
    for i in range(start,end):
        yield i
for _ in my_gen_range(20,50):
    print(_)


gen = (i**2 for i in range(1,100))
for i in gen:
    print(i)
"""
def fib(num):
   x,y = 0,1
   for i in range(num):
       x,y = y,x+y
       yield x
def square(nums):
    for num in nums:
        yield num**2
print(sum(square(fib(20))))


