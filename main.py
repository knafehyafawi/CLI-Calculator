from functions import *

def main():

    num1 = float(input("Enter first number: "))
    operation = input("Enter operation: ")

    if operation in UNARY_OPS:
        ans = calculate(num1, operation, num2=None)
        print(ans)
        return
    elif operation in BINARY_OPS:
        num2 = float(input("Enter second number: "))
        ans = calculate(num1, operation, num2)
        print(ans)
        return

main()