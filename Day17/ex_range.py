# range() is an immutable, memory-efficient sequence used to generate numbers for iteration.
# Syntax1: range(value)
r=range(6)
print(r) # range(0, 6)  0 t0 6-1

print(r,type(r))  # range(0, 6) <class 'range'>

for val in r:
    print(val)

# 0
# 1
# 2
# 3
# 4
# 5


for val in range(6):
    print(val)
# 0
# 1
# 2
# 3
# 4
# 5

for val in range(11):
    print(val)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# Syntax2: range(start, stop)
r=range(10,16)
print(r,type(r)) # range(10, 16) <class 'range'>

for val in r:
    print(val)
# 10
# 11
# 12
# 13
# 14
# 15   

for val in range(100,106):
    print(val)
# 100
# 101
# 102
# 103
# 104
# 105   

# NOTE: The above TWO syntaxes, by default uses+1 step

# Syntax3: range(Start,Stop, Step)

r= range(10,21,2)
print(r,type(r)) # range(10, 21, 2) <class 'range'>

for val in r:
    print(val)
# 10
# 12
# 14
# 16
# 18
# 20

for val in range(100,107,2):
    print(val)

# 100
# 102
# 104
# 106

for val in range(10, 55, 5):
    print(val)

#    10
#    15
#    20
#    25
#    30
#    50
#    35
#    40
#    45

for val in range(-9, 0):
    print(val)

#    -9
#    -8
#    -7
#    -6
#    -5
#    -4
#    -3
#    -2
#    -1

for val in range(-9,0,1):
    print(val)
    # -9
    # -8
    # -7
    # -6
    # -5
    # -4
    # -3
    # -2
    # -1

for val in range(-9,0,2):
    print(val)
    # -9
    # -7
    # -5
    # -3
    # -1

r=range(1000,1041,10)
print(r[0]) # 1000
print(r[-1]) # 1040
print(r[0:3]) # range(1000, 1030, 10)
for val in r[0:3]:
    print(val)

# 1000
# 1010
# 1020

r[0]=120 # TypeError: 'range' object does not support item assignmen

