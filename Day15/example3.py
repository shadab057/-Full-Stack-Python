# - complex()  type 

# int type into complex type -- POSSIBLE
a=123
print(a,type(a)) # 123 <class 'int'>
b=complex(a)
print(b,type(b)) # (123+0j) <class 'complex'>

# float type into complex type -- POSSIBLE
a=3.14
print(a,type(b)) # 3.14 <class 'complex'>
b=complex(b)
print(b,type(b)) # (3.14+0j) <class 'complex'>

# bool type into complex type -- POSSIBLE

a=True
print(a,type(a)) # True <class 'bool'>
b=complex(a)
print(b,type(b)) # (1+0j) <class 'complex'>

a=False
print(a,type(a)) # False <class 'bool'>
b=complex(a)
print(b,type(b)) # 0j <class 'complex'>

# complex type into complex type -- POSSIBLE 
a=3+2j
print(a,type(a)) # (3+2j) <class 'complex'>
b=complex(a)
print(b,type(b)) # (3+2j) <class 'complex'>


# str int type into complex type -- POSSIBLE
a="123"
print(a,type(a)) # 123 <class 'str'>
b=complex(a)
print(b,type(b)) # (123+0j) <class 'complex'>

# str float type into complex type -- POSSIBLE
a="3.14"
print(a,type(a)) # 3.14 <class 'str'>
b=complex(a)
print(b,type(b)) # (3.14+0j) <class 'complex'>

# str bool type into complex type -- NOT POSSIBLE
a="True"
print(a,type(a)) # True <class 'str'>
# b=complex(a)
# print(b,type(b)) # ValueError: complex() arg is a malformed string  

# str type into complex type -- NOT POSSIBLE
a="shad"
print(a,type(a)) # shad <class 'str'>
# b=complex(a)
# print(b,type(b)) # ValueError: complex() arg is a malformed string

# str complex type into complex type -- POSSIBLE 
a="2+3j"
print(a,type(a)) # 2+3j <class 'str'>
b=complex(a)
print(b,type(b)) # (2+3j) <class 'complex'>

a="2+4i"
print(a,type(a)) # (2+4i) <class 'complex'>
b=complex(a) 
print(b,type(b)) # ValueError: complex() arg is a malformed string 

# str pure type into complex type -- NOT POSSIBLE
a="PYTHON"
print(a,type(a)) # PYTHON <class 'str'>
b=complex(a)
print(b,type(b)) # ValueError: complex() arg is a malformed string 





