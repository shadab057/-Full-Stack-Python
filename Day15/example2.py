# bool type

# int type into bool type -- POSSIBLE
a=123
print(a,type(a)) # 123 <class 'int'>
b=bool(a)
print(b,type(b)) # True <class 'bool'>

a=0
print(a,type(a)) # 0 <class 'int'>
b=bool(a)
print(b,type(b)) # False <class 'bool'>

# float type into bool type --  POSSIBLE
a=3.14
print(a,type(a)) # 3.14 <class 'float'>
b=bool(a)
print(b,type(b)) # True <class 'bool'>

# bool type into bool type --  POSSIBLE
a=True
print(a,type(b)) # True <class 'bool'>
b=bool(a)
print(b,type(b)) # True <class 'bool'>

a=False
print(a,type(a)) # False <class 'bool'>
b=bool(a)
print(b,type(b)) # False <class 'bool'>

# complex type into bool type  -- POSSIBLE
a=2+3j
print(a,type(a)) # (2+3j) <class 'complex'>
b=bool(a)
print(b,type(b)) #  True <class 'bool'>


# str int type itno bool type --  POSSIBLE
a="123"
print(a,type(a)) # 123 <class 'str'>
b=bool(b)
print(b,type(b)) # True <class 'bool'>

# str float type into bool type -- POSSIBLE
a="3.14"
print(a,type(a)) # 3.14 <class 'str'>
b=bool(b)
print(b,type(b)) #True <class 'bool'>

a="0.0" 
print(a,type(a))  # 0.0 <class 'str'>
b=bool(a)
print(b,type(b))  # True <class 'bool'>

# str bool type into bool type -- POSSIBLE
a="True"
print(a,type(a)) # True <class 'str'>
b=bool(a)
print(b,type(b)) # True <class 'str'>

a="False"
print(a,type(a)) # False <class 'str'>
b=bool(a)
print(b,type(b)) # True <class 'bool'

# str complex type into bool type -- POSSIBLE
a=2+3j
print(a,type(a)) # (2+3j) <class 'complex'>
b=bool(a)
print(b,type(b)) # True <class 'bool'>

# str str type into bool type -- POSSIBLE
a="shad"
print(a,type(a)) # shad <class 'str'>
b=bool(b)
print(b,type(b))  # True <class 'bool'>

# # str pure str into bool type -- POSSIBLE
a="PYTHON"
print(a,type(a)) # PYTHON <class 'str'>
b=bool(a)
print(b,type(b)) # True <class 'bool'>







