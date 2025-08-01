#11.	Write a script to print factorial of the given number (while).

n=int(input("Enter Number : "))
fact=1
while n>=1:
    fact*=n
    n-=1
print("Factorial =  ", fact)
