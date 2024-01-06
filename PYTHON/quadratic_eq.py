import cmath
a=int(input())
b=int(input())
c=int(input())
q1=(-b+cmath.sqrt(b**2-4*a*c))/(2*a)
q2=(-b-cmath.sqrt(b**2-4*a*c))/(2*a)
print(q1)
print(q2)