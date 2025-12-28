# append() --
# . is accessor operator
# append() is a mutable 


lst=[10, "Rs"]
print(lst, id(lst)) # [10, 'Rs'] 1372168216576
lst.append("Python")
print(lst, id(lst)) # [10, 'Rs', 'Python'] 2536939544576

lst.append(34.56)
print(lst, id(lst)) # [10, 'Rs', 'Python', 34.56] 2536939544576


lst.append(True)
print(lst, id(lst)) # [10, 'Rs', 'Python', 34.56, True] 2536939544576

lst.append([2+3j])
print(lst, id(lst)) # [10, 'Rs', 'Python', 34.56, True, (2+3j)] 2536939544576   


lst=[]
print(lst, id(lst)) # [] 1614317011200
lst.append(10)
lst.append(1.2)
lst.append(True)
print(lst, id(lst)) # [[10, 1.2, True] 2012775301376





