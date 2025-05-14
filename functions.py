import math

BINARY_OPS = {'+','-','*','/','^', '**'}
UNARY_OPS = {'sqrt'}

def calculate(num1, operation, num2=None):
    """
    If the operation is binary, apply operation to num1 and num2.
    If the operation is unary, apply operation to num1.
    ----------
    :param num1:
    :param operation:
    :param num2:
    :return: ans
    ----------
    """
    # ---------- BINARY ----------
    if operation in BINARY_OPS:
        if num2 is None:
            return "Syntax error: please input two operands."

        elif num2 is not None:
            if operation in {'+'}:
                ans = num1 + num2
                return ans
            if operation in {'-'}:
                ans = num1 - num2
                return ans
            if operation in {'*'}:
                ans = num1 * num2
                return ans
            if operation in {'/'}:
                if num2 == 0:
                    return 'Math error. Cannot divide by zero.'
                else:
                    ans = num1 / num2
                    return ans
            if operation in {'^', '**'}:
                ans = num1 ** num2
                return ans

    # ---------- UNARY ----------
    if operation in UNARY_OPS:
        if operation in {'sqrt'}:
            if num2 is not None:
                return "Syntax error: please input only one operand."
            if num1 < 0:
                return "Math error: Cannot square root negative number."

            ans = math.sqrt(num1)
            return ans

    # ---------- UNKNOWN ----------

    return "Syntax error. Operation not recognized."
