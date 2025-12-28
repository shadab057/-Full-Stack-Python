#  remove(): Mutalble method
# It is used to remove the first occurrence of a specific element from the list.    


lst= ['hyd', 10, "RS", 34.56, 'Python']
lst.remove(10)
print(lst, type(lst), id(lst)) # ['hyd', 'RS', 34.56, 'Python'] <class 'list'> 1624259125248

lst.remove('hyd')
print(lst, type(lst), id(lst)) # ['RS', 34.56, 'Python'] <class 'list'> 1624259125248   

lst.remove("Python")
print(lst, type(lst), id(lst)) # ['RS', 34.56] <class 'list'> 1624259125248

lst.reomve("Python")
print(lst, type(lst), id(lst)) # ValueError: list.remove(x): x not in list

