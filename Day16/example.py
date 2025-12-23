# bytes 

# NOT POSSIBLE 
lst=[100,200,300,10,0,256,45,67]
print(lst,type(lst))  # [100, 200, 300, 10, 0, 256, 45, 67] <class 'list'>
# b=bytes(lst)
# print(b,type(b)) # ValueError: bytes must be in range(0, 256)

#  POSSIBLE 
lst=[100,200,10,0,255,45,67]
print(lst,type(lst))  # [100, 200, 10, 0, 255, 45, 67] <class 'list'>
b=bytes(lst)
print(b,type(b)) # b'd\xc8\n\x00\xff-C' <class 'bytes'>

for val in b:
    print(b)  
# b'd\xc8\n\x00\xff-C'
# b'd\xc8\n\x00\xff-C'
# b'd\xc8\n\x00\xff-C'
# b'd\xc8\n\x00\xff-C'
# b'd\xc8\n\x00\xff-C'
# b'd\xc8\n\x00\xff-C'
# b'd\xc8\n\x00\xff-C'

for val in b:
    print(val)
# 100
# 200
# 10
# 0
# 255
# 45
# 67

print(b[1]) # 200
print(b[-1]) # 67
print(b[1:5]) # b'\xc8\n\x00\xff'

for val in b[1:5]:
    print(val) # 200
# 10
# 0
# 255
for val in b[::-1]:
    print(val)
# 67
# 45
# 255
# 0
# 10
# 200
# 100    


# 
a=10
print(a,id(a)) # 10 140712693822664
a=a+1
print(a,id(a)) # 11 140712693822696

lst=[100,200,300,10,0,256,45,67]
print(lst,type(lst),id(lst))  # [100, 200, 300, 10, 0, 256, 45, 67] <class 'list'> 3141415952384
lst[0]=lst[0]+1
print(lst,type(lst), id(lst))

print(b[0]) # 100

b[0]=200
print(b[0]) # TypeError: 'bytes' object does not support item assignment