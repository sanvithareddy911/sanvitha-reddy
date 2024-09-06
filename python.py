python.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Example usage
print("Addition: 5 + 3 =", add(5, 3))
print("Subtraction: 5 - 3 =", subtract(5, 3))
print("Multiplication: 5 * 3 =", multiply(5, 3))
print("Division: 5 / 3 =", divide(5, 3))
