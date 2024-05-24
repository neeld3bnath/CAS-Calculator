from sympy import *
import os

os.system('cmd /k "python & from sympy import init_session & init_session()"')
# os.system('cmd /k "from sympy import init_session"')
# os.system('cmd /k "init_session()"')

print("Welcome to my algebra calculator!")
print("What do you want to do?")

print("1. Solve for a variable")
print("2. Find if a function is even, odd, or neither")
print("3. Find the derivative of a function")
print("4. Find the integral of a function")
print("5. Find the limit of a function")
print("6. Find the roots of a function")
print("7. Solve a system of equations")
print("8. Find the value of a function at an x value")
print("9. Quit")

user = int(input("Enter your choice: "))
if user == 1:
    input2 = input("Enter the equation: ")
    variable = input("Enter the variable: ")
    
if user == 2:
    input2 = input("Enter the function: ")
if user == 3:
    input2 = input("Enter the function: ")
if user == 4:
    input2 = input("Enter the function: ")
if user == 5:
    input2 = input("Enter the function: ")
if user == 6:
    input2 = input("Enter the function: ")
if user == 7:
    input2 = input("Enter the function: ")
if user == 8:
    input2 = input("Enter the function: ")
if user == 9:
    quit()     
