# del operator : Mutable operation
# The del operator is used to delete elements from a list at a specific index or slice.

lst=[10, "RS", "Python", 34.56, True, 2+3j]
print(lst, type(lst),id(lst)) # [10, 'RS', 'Python', 34.56, True, 2+3j] <class 'list'> 1624259125248    
del lst[-3]
print(lst, type(lst), id(lst)) # [10, 'RS', 'Python', True, 2+3j] <class 'list'> 1624259125248  
del lst[2:4]
print(lst, type(lst), id(lst)) # [10, 'RS', 2+3j] <class 'list'> 1624259125248

del lst[::]
print(lst, type(lst), id(lst)) # [] <class 'list'> 1624259125248        

lst= [10, "RS", "Python", 34.56, True, 2+3j]
print(lst, id(lst)) # [10, 'RS', 'Python', 34.56, True, 2+3j] <class 'list'> 1624259125248

del lst
print(lst, id(lst)) # NameError: name 'lst' is not defined

# del on string its a immutable object
# del on string will raise TypeError
# del on string is not allowed
# it's is an immutable operation

s="PYTHON"
print(s, type(s)) # PYTHON <class 'str'>

del s[-2]
print(s, type(s)) # TypeError: 'str' object doesn't support item deletion   

