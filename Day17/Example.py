# Int ()
a=10
print(a, id(a)) # 10 140730394047688
a=a+1
print(a,id(a))  # 11 140730521973992
a=a+1
print(a,id(a))  # 12 140730521974024


# float ()
a=1.2
print(a,id(a)) # 1.2 2959598328464
a=a+1
print(a,id(a)) # 2.2 221033547003

# bool ()
a=True
print(a,id(a)) # True 140730858009008
a=False
print(a,id(a)) # False 140730858009040

# Complex ()
a=2+3j
print(a,id(a)) # (2+3j) 1987259900528
a=a+2
print(a,id(a)) # (4+3j) 1388000549360

# string 
a="PYTHON"
print(a,type(a),id(a)) # PYTHON <class 'str'> 1949202315280
a=a+"PROG"
print(a,type(a),id(a)) # PYTHONPROG <class 'str'> 2297704480048
a[0]
a[0]="J" # TypeError: 'str' object does not support item assignment







