#11.	Write a script to print factorial of the given number (for loop).

n=int(input("Enter Number : "))
fact=1

for i in range(1,n+1):
    fact*=i

print("Factorial =  ", fact)
