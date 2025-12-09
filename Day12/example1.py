a=0.0000000000000000000000000000000000005
print(a,type(a))  # 5e-37 <class 'float'>

a=0.0000000000000000000000025
print(a,type(a))  # 2.5e-24 <class 'float'>


a=0o12.0o34
print(a,type(a))  # invalid literal for float() with base 10: '0o12.0o34'