a = 1
b = 2

c = b # c is pointing to 1
b = a # b is pointing to 2
a = c # b is pointing to 1

print(a)
print(b)