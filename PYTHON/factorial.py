num=int(input())
fact=1
if num<0:
    print("negative number")
elif num==0:
    print("fact of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("fact of",num,"is",fact)