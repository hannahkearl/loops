def add(x: float, y: float) -> float:
    return x + y

def multiply(x: float, y: float) -> float:
    return x * y

def square(x: float) -> float:
    return x * x

def add_squares(x: float, y: float) -> float:
    return add(square(x), square(y))

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

print("Sum:", add(num1, num2))
print("Produt:", multiply(num1, num2))
print("Square of 1st number:",  square(num1))
print("Square of 2nd number:", square(num2))
print("Sum of squares:", add_squares(num1, num2))
