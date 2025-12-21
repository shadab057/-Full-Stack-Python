# - str()  

# int type into str type -- POSSIBLE
a=123
print(a,type(a))  # 123 <class 'int'>
b=str(a)
print(b,type(b)) # 123 <class 'str'>


# float type into str type -- POSSIBLE
a=12.3
print(a,type(a)) # 12.3 <class 'float'>
b=str(a)
print(b,type(b)) # 12.3 <class 'str'>

# bool type into str type -- POSSIBLE
a=True
print(a,type(a)) # True <class 'bool'>
b=str(a)
print(b,type(b)) # True <class 'str'>

# complex type into str type -- POSSIBLE
a=2+3j
print(a,type(a)) # (2+3j) <class 'complex'>
b=str(a)
print(b,type(b)) # (2+3j) <class 'str'>

# str int type into complex type -- POSSIBLE
a="123"
print(a,type(a)) # 123 <class 'str'>
b=str(a)
print(b,type(b)) # 123 <class 'str'>

# str float type into complex type -- POSSIBLE
a="12.4"
print(a,type(a)) # 12.4 <class 'str'>
b=str(a)
print(b,type(b)) # 12.4 <class 'str'>

# str bool type into complex type -- POSSIBLE
a="True"
print(a,type(a)) # True <class 'str'
b=str(a)
print(b,type(b)) # True <class 'str'

# str complex type into complex type -- POSSIBLE
a="2+3j"
print(a,type(a)) # 2+3j <class 'str'
b=str(a)
print(b,type(b)) # 2+3j <class 'str'

# pure complex type into complex type -- POSSIBLE
a="PYTHON"
print(a,type(a)) # PYTHON <class 'str'
b=str(a)
print(b,type(b)) # PYTHON <class 'str'
