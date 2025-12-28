# pop () : Mutable method
# The pop() method removes and returns the element at the specified index from the list.

lst= [10,20, 20, 10, 30,40, 10, 40]
print(lst, type(lst), id(lst)) # [10, 20, 20, 10, 30, 40, 10, 40] <class 'list'> 1624259125248

lst.pop(3)
print(lst, type(lst), id(lst)) # [10, 20, 20, 30, 40, 10, 40] <class 'list'> 1624259125248

lst.pop(2)
print(lst, type(lst), id(lst)) # [10, 20, 30, 40, 10, 40] <class 'list'> 1624259125248


lst.pop(-2)
print(lst,type(lst), id(lst)) # [10, 20, 30, 40, 40] <class 'list'> 1624259125248   

lst.pop(-2)
print(lst,type(lst), id(lst)) # [10, 20, 30, 40] <class 'list'> 1624259125248   

lst.pop(100)
print(lst,type(lst), id(lst)) # IndexError: pop index out of range

lst.pop(-100)
print(lst,type(lst), id(lst)) # IndexError: pop index out of range

[].pop()
print(lst,type(lst), id(lst)) # IndexError: pop from empty list

list().pop()
print(lst,type(lst), id(lst)) # IndexError: pop from empty list 

