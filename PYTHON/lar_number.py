a=int(input())
b=int(input())
c=int(input())
if a<c and b<c:
    print("c is large",c)
elif a>b and a>c:
    print("a is larger",a)
else:
    print("b is larger",b)