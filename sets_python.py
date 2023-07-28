myset = {"apple","bnanas","Mango","Graphes","dates",}
print(myset)
sett = set(("hello","how","Are","You"))
print(sett)
print(type(sett))
for i in myset:
    print(i)
    
print("\n------------------------\n")
print("apple" in myset)
print("bnana" in myset)
myset.add("orange")
print(myset)

myset.update(sett)
print(myset)

print("\n------------------------\n")
mylist = ["EHtsham","Khaliq"]
myset.update(mylist)
print(myset)



"""
#remvoing the element from the set
"""
# myset.remove("bnanas")
# print(x)

thisset = {"Apple","Bnanas","Orange","Dates","Graphes"}
thisset.discard("Apple")#it will not raise an error if this doesnt exist
print(thisset)
#pop method
print("\n------------------------\n")
thisset.pop()
print(thisset)
thisset.pop()#remove random element from the set
print(thisset)

set1 = {"a","b","c","d","f"}
set2 = {1,2,3,4,5,6,"a","b"}
set3 = set1.union(set2)
print(set3)
print("\n------------------------\n")
set4 = set1.intersection(set2)
print(set4)
print("\n------------------------\n")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)
