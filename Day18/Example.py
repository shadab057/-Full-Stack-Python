lst1=[10,20,30,10,20,30,40]
print(lst1, type(lst1))
# [10, 20, 30, 10, 20, 30, 40] <class 'list'>

lst2=[100,"RS",34.56,True,2+3j,]
print(lst2,type(lst2))
# [100, 'RS', 34.56, True, (2+3j)] <class 'list'>

print(lst2[0]) 
# 100

print(lst2[-1])
# (2+3j)
print(lst2[1:4])  # slicing
# ['RS', 34.56, True]

print(lst2[::2]) # slicing with step
# [100, 34.56, (2+3j)]

print(lst2[::-1]) # reverse list
# [(2+3j), True, 34.56, 'RS', 100]

print(lst2[len(lst2)-1])
# (2+3j)
print(lst2[-len(lst2)])
# 100

print(lst2,type(lst2), id(lst2))
# [100, 'RS', 34.56, True, (2+3j)] <class 'list'> 2481155948608
lst2[2]=45.67
print(lst2) 
# [100, 'RS', 45.67, True, (2+3j)]  we can modify list elements 
lst2[1]="Python"
print(lst2)
# [100, 'Python', 45.67, True, (2+3j)]

lst2[1]="Guido van Rossum" # indexed based Assignment
print(lst2, type(lst2), id(lst2))
# [100, 'Guido van Rossum', 45.67, True, (2+3j)] <class 'list'> 2481155948608

'''
# list is mutable, we can change the elements of list
# but the id of list remains same
# list allows duplicate elements
# list allows heterogeneous elements
# '''

print(lst2[2:4])
# [45.67, True]

lst2[2:4]=[55.55, False] # modifying multiple elements using slicing
print(lst2)
# [100, 'Guido van Rossum', 55.55, False, (2+3j)]

