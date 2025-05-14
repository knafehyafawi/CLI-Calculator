import math

BINARY_OPS = {
    '+':lambda a, b: a + b,
    '-':lambda a, b: a - b,
    '*':lambda a, b: a * b,
    '/':lambda a, b: a / b if b!=0 else "Math error: Division by zero.",
    '^':lambda a, b: a ** b,
    '**':lambda a, b: a ** b,
}
UNARY_OPS = {
    'sqrt':lambda a: math.sqrt(a) if a>=0 else "Math error: Cannot square root negative."

}

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

        return BINARY_OPS[operation](num1, num2)

    # ---------- UNARY ----------
    if operation in UNARY_OPS:
        if num2 is not None:
            return "Syntax error: please input one operand."

        return UNARY_OPS[operation](num1)

    # ---------- UNKNOWN ----------
    return "Syntax error. Operation not recognized."
