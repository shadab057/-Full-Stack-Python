# bytearrays

# lst=[100,200,256,0,55,166]
# print(lst) # [100, 200, 256, 0, 55, 166]
# ba=bytearray(lst) # ValueError: byte must be in range(0, 256)

# lst=[100,-200,255,0,55,166]
# print(lst) # ValueError: byte must be in range(0, 256)




lst=[100,200,255,0,55,166]
print(lst,type(lst)) # [100, 200, 255, 0, 55, 166] <class 'list'>
ba=bytearray(lst)
print(ba,type(ba))  # bytearray(b'd\xc8\xff\x007\xa6') <class 'bytearray'>

for val in ba:
    print(val)

# 100
# 200
# 255
# 0
# 55
# 166

lst=[100,200,255,0,55,166]
ba=bytearray(lst)
print(ba,type(ba)) # bytearray(b'd\xc8\xff\x007\xa6') <class 'bytearray'>

print(ba[0]) # 100
print(ba[-1]) # 166

for val in ba[::-1]:
    print(val)

# 166
# 55
# 0
# 255
# 200
# 100

lst=[100,200,255,0,55,166]
ba=bytearray(lst)
print(ba,type(ba),id(ba))  # bytearray(b'd\xc8\xff\x007\xa6') <class 'bytearray'> 2982792592880
print(ba[0]) # 100

ba[0]=150
print(ba,type(ba),id(ba)) # bytearray(b'\x96\xc8\xff\x007\xa6') <class 'bytearray'> 2491052391920

for val in ba:
    print(val)

# 150
# 200
# 255
# 0
# 55
# 166
