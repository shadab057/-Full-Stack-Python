# Mutable

lst=[10,23,45,255,67,89,10]
b=bytes(lst)
for val in b:
    print(val)
# 10
# 23
# 45
# 255
# 67
# 89
# 10

print(b[0]) # 10
# print(b[0]=100) # typeerror: 'bytes' object does not support item assignment

s={10,20,30}
print(s,type(s)) # {10, 20, 30} <class 'set'>

# s[0]=100 # TypeError: 'set' object does not support item assignment
print(s,id(s)) # {10, 20, 30} 1751518937824

s.add(100)
print(s,id(s)) # {100, 10, 20, 30} 3071588238048






