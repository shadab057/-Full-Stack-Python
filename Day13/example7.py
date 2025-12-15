# strobj [Beginindex:]

s="PYTHON"
print(s) # PYTHON

print(s[0:]) # PYTHON
print(s[2:]) # THON
print(s[3:]) # HON
print(s[1:]) # YTHON
print(s[4:]) # ON

######################

print(s[-122:]) # PYTHON
print(s[-2:]) # ON
print(s[-5:]) # YTHON

######################

print(s[True:] )# YTHON
print(s[False:True]) # 'P'
print(s[0xf:]) # ''
print(s[-True:]) # N

#### StrObj[:Endindex] ####

print(s[:5]) # PYTHO
print(s[:3]) # PYT
print(s[:-3]) # PYT
print(s[:-1]) # PYTHO
print(s[:-2]) # PYTH
print(s[:-0]) # ''