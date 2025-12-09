# True=100
# # SyntaxError: cannot assign to True
# False=200
# # SyntaxError: cannot assign to False

# import keyword
# print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert',
#  'async', 'await', 'break', 'class', 'continue',
#  'def', 'del', 'elif', 'else', 'except', 'finally',
#  'for', 'from', 'global', 'if', 'import', 'in',
#  'is', 'lambda', 'nonlocal', 'not', 'or', '    pass', 'raise', 'return',
#  'try', 'while', 'with', 'yield'] 
# len(keyword.kwlist)
# 35


a=True
print(a,type(a))  # True <class 'bool'>
b=False
print(b,type(b))  # False <class 'bool'>

x=10
# z=x+y 
# NameError: name 'y' is not defined

# a=true
# print(a)    
# name 'true' is not defined. Did you mean: 'True'? 

a=True
b=False
c=a+b 
print(c,type(c))  # 1 <class 'int'>

print(True+True)  # 2
print(False+False)  # 0
print(True+True+False)  # 2

print(True+False-True) # 0

print(3*True+2) # 5

print(0b1111+True)

print(0xC-True) # 11

# print(0o8-True)  # SyntaxError: invalid digit '8' in octal literal


print(True/True) # 1.0
print(True//True) # 1

print(False/True) # 0.0
# print(True/False)  # ZeroDivisionError: division by zero   


 
