
"""   """
>>> addr1="""Guido Van Rossum
... FNO:2-4, Hill Side
... Python Software foundation
... Netherland lands-56"""
>>> print(addr1,type(addr1))
Guido Van Rossum
FNO:2-4, Hill Side
Python Software foundation
Netherland lands-56 <class 'str'>



'''     '''

>>> addr2='''James Gosling
... HNO:12-13, SEA SIDE
... USA-18'''
>>> print(addr2,type(addr2))
James Gosling
HNO:12-13, SEA SIDE
USA-18 <class 'str'>


>>> s1="Python Programmig\nDeveloped by Rossum\tAt CWI in NL"
>>> s1="Python Programmig\nDeveloped by Rossum\nAt CWI in NL"
>>> print(s1,type(s1))
Python Programmig
Developed by Rossum
At CWI in NL <class 'str'>

s="""Python Programming"""
print(s,type(s)) # Python Programming <class 'str'>


>>> s="""Python Programming"""
>>> print(s,type(s))
Python Programming <class 'str'>
>>> s
'Python Programming'


>>> s1="""Python Programming
... Dev by Guido Van Rossum
... in netherlands"""
>>> s1
'Python Programming\nDev by Guido Van Rossum\nin netherlands'
>>>