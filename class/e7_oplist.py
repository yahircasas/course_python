# 1. From the given list, replace the number by its name, then print out the list
numbers = [11, 4, 9, 100, 1000]
numbers_names = ['once', 'cuatro', 'nueve', 'cien', 'mil']
numbers.clear()
numbers.extend(numbers_names)
print(numbers)

# Forma del profesor
numbers[0] = 'eleven'
numbers[1] = 'four'
numbers[2] = 'nine'
numbers[3] = 'one hundred'
numbers[4] = 'one thousand'
print(numbers)

# 2. replace all numbers with the numbers 9.6 and 6 with 6 and 9.6 respectively
scores = [9.6, 6, 10, 4.5, 5, 8.2]
index_6 = scores.index(6)
index_9_6 = scores.index(9.6)
scores[index_6] = 9.6
scores[index_9_6] = 6
print(scores)

# profesor
scores[0:2] = [6 , 9.6]
print(scores)

# 3. from the given list, there are two items that do not correspond to the list (notice the contex), delete it
items = ['red', 'purple', 'green', 'yellow', 'phone', 'magenta', 'math', 'white']
# items.pop(items.index('phone'))
# items.pop(items.index('math'))
# print(items)

# profesor
items.remove('phone')
items.remove('math')
print(items)

# 4. delete the numbers from the list, then print out the final list
my_list = ['r', 'e', 5, 8, 'c', 'q', 9]
del my_list[2]
del my_list[2]
del my_list[-1]
print(my_list)


# 5. insert the elements that the variables have. ANSWER: What do you observe?
a = [5, 5, 5]
b = {'key': 1}
c = ('a', 'b')
d = 'jeje'
lst = []

# primera manera
lst.append(a)
lst.append(b)
lst.append(c)
lst.append(d)
print(lst)

# segunda manera
# cont = [a, b, c, d]
# lst += cont
# print(lst)

# 6. Use *= as you want
my_numbers = [5, 6, 7, 8, 9, 10]
my_numbers *= 4
print(my_numbers)

# 7. Print the 1 that are in the lists
nested_list = [[[[1]]]]
print(nested_list[0][0][0][0])

# 8. Print the word
nested_list2 = [[1], [['hello']]]
print(nested_list2[1][0][0])
