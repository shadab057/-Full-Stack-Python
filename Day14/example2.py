s="PYTHON"
print(s[0:6:2]) # PTO
print(s[2:6:3]) # TN
print(s[4:2:2]) # ''
print(s[1:5:3]) # YO
print(s[1:10:2]) # YHN


####################  

print(s[-6:-1:2]) # PTO
print(s[-6:-2:4]) # P
print(s[-5:-1:3]) # YO

# -ve Begin and -ve Ending



####  ####    ####

print(s[0::2]) # PTO
print(s[2::3]) # TN
print(s[3::3]) # H
print(s[-6::2]) # PTO
print(s[-5::1]) # YTHON
print(s[-5::]) # YTHON

# Begin and step end not specify 

print(s[:4:2]) # PT
print(s[:6:3]) # PH
print(s[:3:]) # PYT
print(s[:6:4]) # PO
print(s[:-1:1]) # PYTHO
print(s[-5:2]) # P
print(s[-122:1]) # ''
print(s[122::1]) # ''





