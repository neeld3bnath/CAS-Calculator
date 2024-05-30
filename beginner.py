from sympy import *

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
    print("7. Find the value of a function at an x value")
    print("8. Rationalize the denominator")
    print("9. Quit")

    user = int(input("Enter your choice: "))
    if user == 1:
        print()
        firsthalf = input("Enter the first part of the equation (before the equals sign): ")
        firsthalf = parse_expr(firsthalf)
        secondhalf = input("Enter the second part of the equation (after the equals sign): ")
        secondhalf = parse_expr(secondhalf)
        equation = Eq(firsthalf,secondhalf)
        pprint(solve(equation), use_unicode=True)

    if user == 2:
        print()
        input2 = input("Enter the function: ")
        input2 = parse_expr(input2)
        pprint(diff(input2), use_unicode=True)
    if user == 3:
        print()
        input2 = input("Enter the function: ")
        input2 = parse_expr(input2)
        input3 = input("Enter the variable: ")
        pprint((Integral(input2),x), use_unicode=True)
    if user == 4:
        print()
        input2 = input("Enter the function: ")
        input2 = parse_expr(input2)
        input3 = input("From the left or right? (l/r): ")
        if input3 == "l":
            pprint(limit(input2,x,-oo), use_unicode=True)
        if input3 == "r":
            pprint(limit(input2,x,oo), use_unicode=True)
    if user == 5:
        print()
        input2 = input("Enter the function: ")
        input2 = parse_expr(input2)
        pprint(roots(input2), use_unicode=True)
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
        pprint(solve([equation1,equation2]), use_unicode=True)
    if user == 7:
        print()
        input2 = input("Enter the function: ")
        input2 = parse_expr(input2)
        value = input("Enter the value of x: ")
        pprint(input2.subs(x,value), use_unicode=True)
    if user == 8:
        print()
        input2 = input("Enter the numerator: ")
        input2 = parse_expr(input2)
        input3 = input("Enter the denominator (use sqrt() for square root): ")
        input3 = parse_expr(input3)
        pprint(simplify(input2/input3), use_unicode=True)
    if user == 9:
        print("Goodbye!")
        break