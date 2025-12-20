# int() 

# float into int
a=3.14
b=int(a)
print(b,type(b)) # 3 <class 'int'>

# bool type into int type
c=True
print(c,type(c))
d=int(c)
print(d,type(d))  # 1 <class 'int'>

e=False
f=int(e)
print(f,type(f)) # 0 <class 'int'>

# complex into int
# a=2+3j
# print(a,type(a)) # (2+3j) <class 'complex'>
# b=int(a)
# print(b,type(b)) # TypeError: int() argument must be a string,
# NOT possible



# Case-1: str into int
y="10"
print(y,type(y)) # 10 <class 'str'>
z=int(y)
print(z,type(z)) # 10 <class 'int'>

# Case-2: str float into int - NOT POSSIBLE 
# k="3.14"
# l=int(k) 
# print(l,type(l))  # ValueError: invalid literal for int() with base 10: '123.45'

# Case-3: str bool into int  --- NOT POSSIBLE 
# a="True"
# print(a,type(a)) # True <class 'str'>
# b=int(a)
# print(b,type(b))  # ValueError: invalid literal for int() with base 10: 'True'

# Case-4: str complex into int type  --- NOT POSSIBLE
a="2+3j"
print(a,type(a))  # 2+3j <class 'str'>
# print(a,int(a))   # ValueError: invalid literal for int() with base 10: '2+3j'

# Case-5: pure str into int type -- NOT POSSIBLE
a="PYTHON"
print(a,int(a))  # ValueError: invalid literal for int() with base 10: 'PYTHON'





