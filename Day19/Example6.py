# index() ---> enumerate() : Immutable method
# The enumerate() method adds a counter to an iterable and returns it in a form of enumerating object.

lst=[10,20,30,40,10,5,60,10,20,10]
print(lst, id(lst)) # [10, 20, 30, 40, 10, 5, 60, 10, 20, 10] 1624259125248 

lst.index(10)
print(lst.index(10)) # 0
lst.index(200)
print(lst.index(200)) # ValueError: 200 is not in list
