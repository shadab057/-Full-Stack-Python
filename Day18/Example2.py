lst=[100, "Rs"]
print(lst, type(lst)) # [100, 'Rs'] <class 'list'>


print(len(lst))  # 2


# --- Empty List ---
lst=[]
print(lst,type(lst), len(lst)) # [] <class 'list'> 0
lst = list()
print(lst,type(lst), len(lst)) # [] <class 'list'> 0


lst = [                 ] 
print(lst, type(lst), len(lst)) # [] <class 'list'> 0


lst= ["  "]
print(lst, type(lst), len(lst)) # ['  '] <class 'list'> 1

lst= [0]
print(lst, type(lst[0]), len(lst)) # [0] <class 'list'> 1
# Yes — an empty list does take some memory.

s="MISSISSIPPI"
print(s,type(s)) # MISSISSIPPI <class 'str'>

lst=list(s)
print(lst, type(lst), len(lst)) # ['M', 'I', 'S', 'S', 'I', 'S', 'S', 'I', 'P', 'P', 'I'] <class 'list'> 11

s="ABRAKADABRA"
lst=list(s)
print(lst, type(lst), len(lst)) # ['A', 'B', 'R', 'A', 'K', 'A', 'D', 'A', 'B', 'R', 'A'] <class 'list'> 11

lst=[10,20,30,40]
b=bytes(lst)
print(b, type(b)) # b'\n\x14\x1e(' <class 'bytes'>
print(lst, type(lst)) #  [10, 20, 30, 40] <class 'list'>



# Syntax2: listobj=list(object)

a=10
print(a,type(a))  # 10 <class 'int'>
# lst=list(a)  # TypeError: 'int' object is not iterable

# str to list typecasting
s="HELLO"
print(s,type(s)) # HELLO <class 'str'>
lst=list(s) # HELLO <class 'str'>

# float to list typecasting
f=12.34
print(f,type(f))  # 12.34 <class 'float'>
# lst=list(f) # TypeError: 'float' object is not iterable

# bool to list typecasting

b=True
print (b,type(b)) # True <class 'bool'>
# lst=list(b) # TypeError: 'bool' object is not iterable

# complex to list typecasting
c=2+3j
print(c,type(c))  # (2+3j) <class 'complex'>
# lst=list(c) # TypeError: 'complex' object is not iterable

lst=list([10])
print(lst,type(lst)) # [10] <class 'list'>

lst=list([12.89])
print(lst,type(lst)) # [12.89] <class 'list'>

lst=list([True]) 
print(lst, type(lst)) # [True] <class 'list'>


s="MISSISSIPPI"
print(s,type(s)) # MISSISSIPPI <class 'str'>
lst=list(s)
print(lst, type(lst))
    # ['M', 'I', 'S', 'S', 'I', 'S', 'S', 'I', 'P', 'P', 'I'] <class 'list'>
lst=list([s])
print(lst, type(lst))
    # ['MISSISSIPPI'] <class 'list'>



 





