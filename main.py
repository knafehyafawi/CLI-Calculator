from pandas.core.ops import arithmetic_op

from functions import *

def main():

    value1 = input("Enter first number: ")

    # select mode: addition, subtraction, etc
    arithmetic_method = input()
    if arithmetic_method == "+":
        print("+")
    if arithmetic_method == "-":
        print("-")
    if arithmetic_method == "*":
        print("*")
    if arithmetic_method == "/":
        print("/")

    value2 = input("Enter second number: ")

    return