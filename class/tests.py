# ## Sum a positive numbers.
# summ = 0
# while True:
#     number = int(input('Enter a number: '))
#     if number <0:
#         print(summ)
#         break
#     summ += number
#
#29/04/2024
# x = 0
# def increment_by_n (n):
#     global x
#     x += n
#     return x
# print(x, increment_by_n(5))
# print(x)

# x = 0
# def increment_by_2n(n):
#     return 2*n
#     x += increment_by_2n(5)
# print(x)

# print(complex(real = 5, imag =5))

# import numpy
# e = numpy.e
# print(e)

# import matplotlib.pyplot as plt
# no se incluyen iterables con asterisco
# names=['jake', 'esteban', 'fred', 'Tim'] #Lista
# corrected_names=map(lambda name: name.title(), names) #Iteratos
# print(list(corrected_names)) #we can use list or tuple SPG
#
# for item in corrected_names:
#     print(item)
# #  se incluyen iterables con asterisco

# for item in map(
#     lambda x,y, d: 2*x**y-d,
#     [1, 2, 3],
#     [0.1, 0.2, 0.3],
#     [0.1, 0.2, 0.3]):
#     print(item)

# def my_fuc(*numbers, **letters):
#     return numbers
# a=my_fuc(5,7,9,20, a=1, b=5)
# print(a)

days = ('Monday', 'Tuesday', 'Wendnesday', 'Thursday', 'Friday')
rest, *school, free = days
print(rest)
print(school)
print(free)









