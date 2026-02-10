"""When all the length of the sides of the triangle is known - a,b,c
semi perimeter (s)= (a+b+c)/2
area =  square root of (s*(s-a)*(s-b)*(s-c)) """
a=float(input("Enter first side of triangle: "))
b=float(input("Enter second side of triangle: "))
c=float(input("Enter third side of triangle: "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c)) ** 0.5
print("Area of triangle gives side is ",round(area,2))