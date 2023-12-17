# ------------lambda  function-----------
from functools import reduce
square = lambda x:x**2
print(square(10))
sum = lambda x,y:x+y
print(sum(10,20))
str = lambda x:x[0]=="a"
print(str("apple"))
print(str("Ehtsham"))


number = lambda x:x.split("-")
print(number("20-30"))

EvenOdd = lambda x:"Even" if x%2==0 else "Odd"
print(EvenOdd(20))
print(EvenOdd(19))


#------Higher order function
def printSum(func,list):
    result = 0
    for i in list:
        if func(i):
            result = result+i
    return result

listt = [11,12,14,15,16,17,18,19,20,22]
xfunc = lambda x:x%2==0
yfunc = lambda x:x%2!=0
zfunc = lambda x:x%3==0

print(printSum(xfunc,listt))
print(printSum(yfunc,listt))
print(printSum(zfunc,listt))


#-------------Higher order function in python----------------------

listt = [2,4,6,7,8,9,10]
print(list(map(lambda x:x*2,listt)))

#2nd Example
students = [
        {
        'name':'Ehtsham khaliq',
        'Father name':'Abdul khaliq',
        'address':'Layyah',
        },
        {
            'name':'Mudassar khaliq',
            'Father name':'Abdul khaliq',
            'address':'Layyah',
        },
        {
            'name':'Asif ali',
            'Father name':'zahoor Ahmad',
            'address':'Narowal',
        }
]
print(list(map(lambda x:x['name'],students)))
#-------------------Filter function in python---------------------
list2 = [2,4,6,7,8,9,10]
print(list(filter(lambda x:x>7,list2)))
#Reduce higher order function
list3 = [12,34,56,11,21,58]
print(reduce(lambda x,y:x+y,list3))
print(reduce(lambda x,y:x if x>y else y,list3))

#list comprehension
list4 = [3,4,5,6,7,8,9,10]
list5 = [item**2 for item in list4]
print(list5)

list6 = [item**2 for item in list4 if item&2!=0]
print(list6)
