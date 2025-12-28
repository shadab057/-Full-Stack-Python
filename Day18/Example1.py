lst=[10,"Rs",34.56, True, 2+3j]
print(lst, type(lst))  # [10, 'Rs', 34.56, True, (2+3j)] <class 'list'>

# Indexing (0-based)
print(lst[0]) # 10

# slicing with step
print(lst[::2])  # [10, 34.56, (2+3j)]

lst[::2] = [1000, 44.44, -4-4.5j]
print(lst) # [1000, 'Rs', 44.44, True, (-4-4.5j)]  # modifying multiple elements using slicing with step



# Modifying Lists

fruits = ["apple", "banana", "cherry"]
print(fruits)  # ['apple', 'banana', 'cherry']

fruits[1] = "blueberry"
print(fruits)
# print(fruits)  ['apple', 'blueberry', 'cherry']

fruits[1:3] = ["kiwi", "mango"]
print(fruits)  # ['apple', 'kiwi', 'mango']



