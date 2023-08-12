import math

def daraje2(a, b, c):
    dis = b**2 - 4*a*c
   
    if dis > 0:
        root1 = (-b + math.sqrt(dis)) / (2*a)
        root2 = (-b - math.sqrt(dis)) / (2*a)
        return root1, root2
    elif dis == 0:
        root = -b / (2*a)
        return root
    else:
        return "No real roots"

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))
roots = daraje2(a, b, c)
print("Root(s):", roots)
