"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *



# Your code goes here
while True:
    math_function = raw_input(">>> ")
    math_function = math_function.split(" ")
    math = ["+", "q", "-", "*", "/", "square","cube", "pow", "mod"]
    if math_function[0] not in math or math_function[1] == None or not math_function[1].isdigit() or not math_function[2].isdigit():
        print "That's not a viable input that we know of. Please try again. >>>"
        continue
    if math_function[0] == "q":
        break
    arg_1 = int(math_function[1])
    if math_function[0] == "+":
        arg_2 = int(math_function[2])
        print add(arg_1, arg_2)
    elif math_function[0] == "-":
        arg_2 = int(math_function[2])       
        print subtract(arg_1, arg_2)   
    elif math_function[0] == "*":
        arg_2 = int(math_function[2])
        print multiply(arg_1, arg_2)
    elif math_function[0] == "/":
        arg_2 = int(math_function[2])
        if arg_2 == 0:
            print "Division by zero is undefined."
            continue
        print divide(arg_1, arg_2)
    elif math_function[0] == "square":
        print square(arg_1)
    elif math_function[0] == "cube":
        print cube(arg_1)
    elif math_function[0] == "pow":
        arg_2 = int(math_function[2])
        print power(arg_1, arg_2)    
    elif math_function[0] == "mod":
        arg_2 = int(math_function[2])
        print mod(arg_1, arg_2)
 
        



