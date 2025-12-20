# float()

#  int type into  float type  --- POSSIBLE
a=12.34
b= int(a)
print(b,int(b)) # 12 12
print(b,type(b))  # 12 <class 'int'>

# Bool type into float type -- POSSIBLE
a=True
print(a,type(a))  # True <class 'bool'>
b=float(a)
print(b,type(b)) # 1.0 <class 'float'>

# Complex type into float type -- NOT POSSIBLE
a=2+3j
print(a,type(a)) # (2+3j) <class 'complex'>
# b=float(a)
# print(b,type(b)) # TypeError: float() argument must be a string or a real number, not 'complex'

# str int type itno float type --  POSSIBLE
a="123"
print(a,type(a)) # 123 <class 'str'>
b=float(b)
print(b,type(b)) # 1.0 <class 'float'>

# str float type into float type -- POSSIBLE
a="3.14"
print(a,type(a)) # 3.14 <class 'str'>
b=float(b)
print(b,type(b)) # 1.0 <class 'float'>

# str Bool type into float type -- NOT POSSIBLE
a="True"
print(a,type(a)) # True <class 'str'>
# b=float(a)
# print(b,type(b)) # ValueError: could not convert string to float: 'True'

# str complex type into float type -- NOT POSSIBLE
a=2+3j
print(a,type(a)) # (2+3j) <class 'complex'>
# b=float(a)
# print(b,type(b)) # TypeError: float() argument must be a string or a real number, not 'complex'

# str str type into float type -- POSSIBLE
a="shad"
print(a,type(a)) # shad <class 'str'>
b=float(b)
print(b,type(b))  # 1.0 <class 'float'>

# str pure str into float type --
a="PYTHON"
print(a,type(a)) # PYTHON <class 'str'>
b=float(a)
print(b,type(b)) # ValueError: could not convert string to float: 'PYTHON'









