mydict = {
    "model":2020,
    "name":"CIVIC",
    "driver":"EHtsham",
    "model":2020,
}
print(mydict)

#we can also store the list in the dictionary
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict['colors'])
print(type(thisdict))

dictionary = dict(name="EHtsham",age=21,department="BSCS")
print(dictionary)
print(dictionary.get("name"))
print(thisdict.keys())
print(thisdict.values())
dictionary["name"] = "Mudassar"
print(dictionary)

thisdict.items()

#update method
thisdict.update({"brand":"Engine"})
print(thisdict)
#Adding element in dictionary
thisdict['colors'] = "red"
print(thisdict)
#pop method is used to remove
thisdict.pop("colors")
thisdict.popitem()#it removes the last item in the dict
print(thisdict)
#del keyword delete the dictionary completely
#del dictionary
#print(dictionary)--->not defined because it has deleted


#clear method make the dictionary empty
thisdict.clear()
print(thisdict)

"""
#Loop and dictionary
"""
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
for i in thisdict.values():
    print(i)
print("\n------------------\n")
for i in thisdict.keys():
    print(i)
print("\n------------------\n")
for (x,y) in thisdict.items():
    print(x,y)
print("\n------------------\n")
mydict2 = mydict.copy()
print(mydict2)
print("\n------------------\n")
dictionary = dict(mydict)
print(dictionary)
print("\n------------------\n")

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
myfamily["child3"]["year"]


x = ('key1', 'key2', 'key3')
y = 2

thisdict = dict.fromkeys(x, y)

print(thisdict)
