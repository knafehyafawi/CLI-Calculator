from functions import *

def __main__():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation: ")
    ans = calculate(num1, num2, operation)
    print(ans)
    return

__main__()