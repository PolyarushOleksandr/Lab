# to run file write in terminal: python Lab1/lr2_ex_2_145.py
a = float(input("Enter a number a: "))
b = float(input("Enter a number b: "))
c = float(input("Enter a number c: "))

D = (b ** 2) - (4 * a * c)
if D < 0:
        print("No roots")
elif D == 0:
        x = -b / (2 * a)
        print("One root:", x)
else:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        print("Two roots:", f"x1={x1:.2f}, x2={x2:.2f}")