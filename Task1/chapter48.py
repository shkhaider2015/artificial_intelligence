def add_Numbers(num1 , num2):
    return num1 + num2

def subtract_Numbers(num1, num2):
    return num1 - num2

def multi_Numbers(num1, num2):
    return num1 * num2

def devide_Numbers(num1, num2):
    return num1 / num2

x = int(input("Enter First Number"))
y = int(input("Enter Second Number"))

addition = add_Numbers(x , y)
subtraction = subtract_Numbers(x, y)
multiplication = multi_Numbers(x, y)
division = devide_Numbers(x, y)

print(addition)
print(subtraction)
print(multiplication)
print(division)