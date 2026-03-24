def divide(a, b):
    if b == 0:
        return "Division by zero is not possible"
    return a / b

def display_divide(a, b):
    result = divide(a, b)
    print("Division =", result)
