#factorial of non-negative integer n, denoted by n! is the product of all positive integers less than or equal to n.
#when a function called itself is called recursive function
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the number:"))
result=fact(n)
print("factorial of",n,"is",result)