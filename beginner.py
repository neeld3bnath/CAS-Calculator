from sympy import *
from sympy import simplify

init_printing()
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')

print("Welcome to my algebra calculator!")
while True:
    print("What do you want to do?")

    print("1. Solve for a variable in an equation")
    print("2. Find the derivative of a function")
    print("3. Find the integral of a function")
    print("4. Find the limit of a function")
    print("5. Find the roots of a function")
    print("6. Solve a system of equations")
    print("7. Find the y-value of a function at an x value")
    print("8. Rationalize the denominator")
    print("9. Graph a rectangular function")
    print("10. Graph a parametric function")
    print("11. Factor an expression")
    print("12. Find the exact value of a trig function (may return something useless)")
    print("13. Solve an inequality")
    print("14. Evaluate an expression")
    print("15. Quit")

    user = int(input("Enter your choice: "))
    if user == 1:
        print()
        firsthalf = input("Enter the first part of the equation (before the equals sign): ")
        firsthalf = parse_expr(firsthalf)
        secondhalf = input("Enter the second part of the equation (after the equals sign): ")
        secondhalf = parse_expr(secondhalf)
        equation = Eq(firsthalf,secondhalf)
        symbol = input("Enter the variable you like to solve for: ")
        pprint(solve(equation,symbol))
    if user == 2:
        print()
        function = input("Enter the function: ")
        function = parse_expr(function)
        pprint(diff(function))
    if user == 3:
        print()
        function = input("Enter the function: ")
        function = parse_expr(function)
        symbol = input("Enter the variable: ")
        pprint((Integral(function),symbol))
    if user == 4:
        print()
        func = input("Enter the function: ")
        func = parse_expr(func)
        symbol = input("Enter the variable: ")
        lim = input("From the left or right? (l/r): ")
        if lim == "l":
            pprint(limit(func,symbol,-oo))
        if lim == "r":
            pprint(limit(func,symbol,oo))
    if user == 5:
        print()
        expression = input("Enter the expression: ")
        expression = parse_expr(expression)
        symbol = input("Enter the variable: ")
        symbol = parse_expr(symbol)
        pprint(roots(expression,symbol))
    if user == 6:
        print()
        fhalf1 = input("Enter the first half of the first equation: ")
        fhalf1 = parse_expr(fhalf1)
        shalf1 = input("Enter the second half of the first equation: ")
        shalf1 = parse_expr(shalf1)
        fhalf2 = input("Enter the first half of the second equation: ")
        fhalf2 = parse_expr(fhalf2)
        shalf2 = input("Enter the second half of the second equation: ")
        shalf2 = parse_expr(shalf2)
        equation1 = Eq(fhalf1,shalf1)
        equation2 = Eq(fhalf2,shalf2)
        pprint(solve([equation1,equation2]))
    if user == 7:
        print()
        func = input("Enter the function: ")
        func = parse_expr(func)
        value = input("Enter the value of x: ")
        pprint(func.subs(x,value))
    if user == 8:
        print()
        numerator = input("Enter the numerator: ")
        numerator = parse_expr(numerator)
        denominator = input("Enter the denominator (use sqrt() for square root if needed): ")
        denominator = parse_expr(denominator)
        pprint(simplify(numerator/denominator))
    if user == 9:
        print()
        func = input("Enter the function of x: ")
        func = parse_expr(func)
        boundary = input("Do you want to set boundaries on the domain? (y/n): ")
        if boundary == "y":
            lower = float(input("Enter the lower bound: "))
            upper = float(input("Enter the upper bound: "))
            plot(func, (x, lower, upper), title=r"$%s$" %latex(func))
        elif boundary == "n":
            plot(func, (x, -10, 10), adaptive=True, title=r"$%s$" %latex(func))
    if user == 10:
        print()
        funcx = input("Enter the x-function (make u the variable): ")
        funcx = parse_expr(funcx)
        funcy = input("Enter the y-function (make u the variable): ")
        funcy = parse_expr(funcy)
        boundary = input("Do you want to set boundaries on the domain? (y/n): ")
        if boundary == "y":
            lower = float(input("Enter the lower bound: "))
            upper = float(input("Enter the upper bound: "))
            plot_parametric((funcx, funcy), (u, lower, upper))
        elif boundary == "n":
            plot_parametric((funcx, funcy), (u, -10, 10), adaptive=True)
    if user == 11:
        print()
        expression = input("Enter the expression: ")
        expression = parse_expr(expression)
        pprint(factor(expression))
    if user == 12:
        print()
        trig = input("What trig function do you want to find the exact value of? (sin, cos, tan, cot, sec, csc): ")
        print("\nYou can use 'sqrt()' for square root or 'pi' for pi.")
        trig_functions = {"sin": sin, "cos": cos, "tan": tan, "cot": cot, "sec": sec, "csc": csc}
        trig_function = trig_functions.get(trig)
        if trig_function:
            input3 = input("Enter the value (must be in radians): ")
            answer = trig_function(parse_expr(input3))
            if answer.equals("zoo"):
                print("Value is undefined.")
            else:
                pprint(answer)
        else:
            print("Invalid input.")
    if user == 13:
        print()
        print("You can use >, >=, <, and <=.")
        inequality = input("Enter the inequality: ")
        inequality = parse_expr(inequality)
        symbol = input("Enter the variable: ")
        symbol = parse_expr(symbol)
        pprint(reduce_inequalities(inequality,symbol))
    if user == 14:
        print()
        expression = input("Enter the expression: ")
        expression = parse_expr(expression)
        pprint(simplify(expression))
    if user == 15:
        print("Goodbye!")
        break