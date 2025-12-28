# 5. pop() : Mutable method
# The pop() method removes and returns the last element from the list.

lst=[10, 20, 20, 10, 30, 40, 10, 40]
print(lst, type(lst), id(lst)) # [10, 20, 20, 10, 30, 40, 10, 40] <class 'list'> 1624259125248
lst.pop()
print(lst, type(lst), id(lst)) # [10, 20, 20, 10, 30, 40, 10] <class 'list'> 1624259125248
lst.pop()
print(lst, type(lst), id(lst)) # [10, 20, 20, 10, 30, 40] <class 'list'> 1624259125248

lst.pop()
print(lst, type(lst), id(lst)) # [10, 20, 20, 10, 30] <class 'list'> 1624259125248
lst.pop()       
print(lst, type(lst), id(lst)) # [10, 20, 20, 10] <class 'list'> 1624259125248



lst=[10,20, 30]
print(lst, type(lst), id(lst)) # [10, 20, 30] <class 'list'> 1624259125248
lst.pop()       
print(lst, type(lst), id(lst)) # [10, 20] <class 'list'> 1624259125248

[].pop()
print(lst, type(lst), id(lst)) # IndexError: pop from empty list    
