lst=[10, 20, 20, 10, 30, 40, 10, 40]
print(lst, id(lst)) # [10, 20, 20, 10, 30, 40, 10, 40] <class 'list'> 1624259125248
lst.remove(10)
print(lst, type(lst), id(lst)) # [20, 20, 10, 30, 40, 10, 40] <class 'list'> 1624259125248  

# first occurance specific element will be removed
lst.remove(20)
print(lst, type(lst), id(lst)) # [20, 10, 30, 40, 10, 40] <class 'list'> 1624259125248

[].remove(100)
print(lst, type(lst), id(lst)) # ValueError: list.remove(x): x not in list      

list().remove("Python")
print(lst, type(lst), id(lst)) # ValueError: list.remove(x): x not in list  




