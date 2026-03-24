import add
import sub
import multiply
import divide

num1 = 20
num2 = 10

print("Addition =", add.add(num1, num2))
print("Subtraction =", sub.subtract(num1, num2))
print("Multiplication =", multiply.multiply(num1, num2))
print("Division =", divide.divide(num1, num2))

print()

add.display_add(num1, num2)
sub.display_subtract(num1, num2)
multiply.display_multiply(num1, num2)
divide.display_divide(num1, num2)
