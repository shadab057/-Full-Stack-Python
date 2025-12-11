
# Indexing

s="Python PROG"
len(s)  #11
s="Python PROG"
print(s[0]) # 'P'
print(s[len(s)-1]) # 'G'
print(s[-1]) # 'G'
print(s[-len(s)])  # 'P'

print(s[len(s)-2])  # 0
print()


s1="Python PROG"
print(s1,type(s1))  # Python PROG <class 'str'>

# print(s1[0]) # P
# print(s1[2]) # t

s1[0]  # 'P'
s1[2] # 't'

s1[8]  # IndexError: string index out of range

s1[-3] #'R'

s1[-5] # ' '

s1[len(s1)-1] # SyntaxError: invalid syntax
