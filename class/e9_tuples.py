# 1. With the given list, make a tuple, print out the tuple and print out some element of the tuple
list1 = [1, 2, 3]
my_tuple= tuple(list1)
print(my_tuple)
print(my_tuple[1])

# 2. With the given list, make a tuple, print out the element with index 4 and make it upper
list2 = ['hello', 'math', 'computer', 'Dickens', 'python']
my_tuple2 = tuple(list2)
print(my_tuple2[4].upper())

# 3. Make an example using index() method with a tuple
list2 = ['hello', 'math', 'computer', 'Dickens', 'python']
my_tuple3 = tuple(list2)
print(my_tuple3.index('math'))

# 4. Make an example using count() method with a tuple
print(my_tuple3.count('hello'))