print("Enter sides of the triengle\n a:")
a=float(input())
print("Enter sides of the triengle b:\n")
b=float(input())
print("Enter sides of the triengle:\n")
c=float(input())
s=(a+b+c)/2
Area=(s*(s-a)*(s-b)*(s-c)) ** 0.5
print("Area of your triengle is :%0.3f" %Area)
