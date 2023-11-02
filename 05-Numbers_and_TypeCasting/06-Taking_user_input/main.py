# 01
x = 10
y = 10.10
z = 10j

print(type(x)) 
print(type(y)) 
print(type(z)) 
# 02
x = 10
y = 10.10
z = 10j

a = float(x)
print(a)
print(type(a))
# 03
x = 10
y = 10.10
z = 10j

b = int(y)
print(b)
print(type(b))
# 04
x = 10
y = 10.10
z = 10j

c = complex(x)
print(c)
print(type(c))
# 06
a = "20"
b = "23"
print(a + b) # 2023

# type conversion string into int
print(int(a)+int(b)) # 43

print(int(a)+b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 07
string = "15"
number = 10
string_number = int(string)
sum = number + string_number
print("the sum of both the numbers is: ", sum)