num=int(input("Enter a num"))
fact=1
if num<0:
    print("Factorial of a negative no. doesn't exist")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial of a num",num,"is",fact)

