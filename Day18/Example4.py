# 2.insert() :Mutalble method
# It is used to insert an element at a specific index in the list.

lst=[10,"RS", 34.56,"Python"]
print(lst, id(lst)) # [10, 'RS', 34.56, 'Python'] 1624259125248

lst.insert(2, "PYthon")
print(lst, type(lst), id(lst))  # [10, 'RS', 'PYthon', 34.56, 'Python'] <class 'list'> 1496667742208

lst.insert(1,"GUIDO")
print(lst, type(lst), id(lst))  # [10, 'GUIDO', 'RS', 'PYthon', 34.56, 'Python'] <class 'list'> 149

lst= [10, "RS", 34.56]
print(lst, type(lst),id(lst)) # 

lst.insert(-1, "PYTHON")
print(lst, type(lst), id(lst)) # [10, 'RS', 'PYTHON', 34.56] <class 'list'>

lst.insert(-2, "HTML")
print(lst, type(lst), id(lst)) # [10, 'RS', 'HTML', 'PYTHON', 34.56] <class 'list'><class 'list'> 1624259125248     

lst.insert(100, "PYTHON")
print(lst, type(lst, id((lst)))) # [10, 'RS', 'HTML', 'PYTHON', 34.56, 'PYTHON'] <class 'list'> 1624259125248   

lst.insert(-100, "PYTHON")
print(lst, type(lst, id((lst)))) # ['PYTHON', 10, 'RS', 'HTML', 'PYTHON', 34.56, 'PYTHON'] <class 'list'> 1624259125248 
