def calculate(num1, num2, operation):
    if operation == '+':
        ans = num1 + num2
    elif operation == '-':
        ans = num1 - num2
    elif operation == '*':
        ans = num1 * num2
    elif operation == '/':
        if num2 == 0:
            ans = "Syntax error. Cannot divide by zero."
        else:
            ans = num1 / num2
    else:
        ans = "Syntax error. Operation not recognized."
    return ans