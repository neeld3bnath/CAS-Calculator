from sympy import *
import matplotlib.pyplot as plt
import numpy as np

init_printing()
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')

print("Welcome to my algebra calculator!")
while True:
    print("What do you want to do?")

    print("1. Solve for a variable")
    print("2. Find the derivative of a function")
    print("3. Find the integral of a function")
    print("4. Find the limit of a function")
    print("5. Find the roots of a function")
    print("6. Solve a system of equations")
    print("7. Find the y-value of a function at an x value")
    print("8. Rationalize the denominator")
    print("9. Graph a function")
    print("10. Factor an expression")
    print("11. Find the exact value of a trig function (may return something useless)")
    print("12. Solve an inequality")
    print("13. Quit")

    user = int(input("Enter your choice: "))
    if user == 1:
        print()
        firsthalf = input("Enter the first part of the equation (before the equals sign): ")
        firsthalf = parse_expr(firsthalf)
        secondhalf = input("Enter the second part of the equation (after the equals sign): ")
        secondhalf = parse_expr(secondhalf)
        equation = Eq(firsthalf,secondhalf)
        pprint(solve(equation))

    if user == 2:
        print()
        input2 = input("Enter the function: ")
        input2 = parse_expr(input2)
        pprint(diff(input2))
    if user == 3:
        print()
        input2 = input("Enter the function: ")
        input2 = parse_expr(input2)
        input3 = input("Enter the variable: ")
        pprint((Integral(input2),x))
    if user == 4:
        print()
        input2 = input("Enter the function: ")
        input2 = parse_expr(input2)
        input3 = input("From the left or right? (l/r): ")
        if input3 == "l":
            pprint(limit(input2,x,-oo))
        if input3 == "r":
            pprint(limit(input2,x,oo))
    if user == 5:
        print()
        input2 = input("Enter the expression: ")
        input2 = parse_expr(input2)
        input3 = input("Enter the variable: ")
        input3 = parse_expr(input3)
        pprint(roots(input2,input3))
    if user == 6:
        print()
        fhalf1 = input("Enter the first half of the first equation: ")
        fhalf1 = parse_expr(fhalf1)
        fhalf2 = input("Enter the second half of the first equation: ")
        fhalf2 = parse_expr(fhalf2)
        shalf1 = input("Enter the first half of the second equation: ")
        shalf1 = parse_expr(shalf1)
        shalf2 = input("Enter the second half of the second equation: ")
        shalf2 = parse_expr(shalf2)
        equation1 = Eq(fhalf1,fhalf2)
        equation2 = Eq(shalf1,shalf2)
        pprint(solve([equation1,equation2]))
    if user == 7:
        print()
        input2 = input("Enter the function: ")
        input2 = parse_expr(input2)
        value = input("Enter the value of x: ")
        pprint(input2.subs(x,value))
    if user == 8:
        print()
        input2 = input("Enter the numerator: ")
        input2 = parse_expr(input2)
        input3 = input("Enter the denominator (use sqrt() for square root): ")
        input3 = parse_expr(input3)
        pprint(simplify(input2/input3))
    if user == 9:
        print()
        input2 = input("Enter the function to graph: ")
        input2 = parse_expr(input2)
        boundary = input("Do you want to set boundaries on the domain? (y/n): ")
        if boundary == "y":
            lower = float(input("Enter the lower bound: "))
            upper = float(input("Enter the upper bound: "))
            p = plot(input2, (x,lower,upper))
        elif boundary == "n":
            p = plot(input2)
    if user == 10:
        print()
        input2 = input("Enter the expression: ")
        input2 = parse_expr(input2)
        pprint(factor(input2))
    if user == 11:
        print()
        input2 = input("What trig function do you want to find the exact value of? (sin, cos, tan, cot, sec, csc): ")
        print("\nYou can use 'sqrt()' for square root or 'pi' for pi.")
        trig_functions = {"sin": sin, "cos": cos, "tan": tan, "cot": cot, "sec": sec, "csc": csc}
        trig_function = trig_functions.get(input2)
        if trig_function:
            input3 = input("Enter the value (must be in radians): ")
            answer = trig_function(parse_expr(input3))
            if answer.equals("zoo"):
                print("Value is undefined.")
            else:
                pprint(answer)
    if user == 12:
        print()
        print("You can use >, >=, <, and <=.")
        input2 = input("Enter the inequality: ")
        input2 = parse_expr(input2)
        input3 = input("Enter the variable: ")
        input3 = parse_expr(input3)
        pprint(reduce_inequalities(input2,input3))
    if user == 13:
        print("Goodbye!")
        break