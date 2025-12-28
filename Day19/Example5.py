# clear() : Mutable method
# It is used to remove all elements from the list, resulting in an empty list.  

lst=[10, "Rs", "Python", 34.56, True, 2+3j]
print(lst, type(lst), id(lst)) # [10, 'Rs', 'Python', 34.56, True, 2+3j] <class 'list'> 1624259125248
lst.clear()     
print(lst, type(lst), id(lst)) # [] <class 'list'> 1624259125248
len(lst)
print(len(lst)) # 0

[].clear()
print([].clear()) # None

list().clear()
print(list().clear()) # None




lst=[10, 20, 30, 10, 20,30,10,20,30]
print(lst) # [10, 20, 30, 10, 20, 30, 10, 20, 30]

# delete duplicates from list
S=set(lst)
print(S, type(S)) # {10, 20, 30} <class 'set'>
