import cmath
a=float(input("Enter Cofficient of x**2 -> \'a\'"))
b=float(input("Enter Cofficient of x -> \'b\'"))
c=float(input("Enter Constant \'c\'"))
root1= (-b+(b*b - 4*a*c)**0.5)/2*a
root2= (-b+(b*b + 4*a*c)**0.5)/2*a
print("Roots of the given quadratic is given {0} {1}" .format(root1,root2))
