#12.	Write a script to calculate the sum of all numbers
# from 1 to a given number (while, for).

n=int (input("Enter Number : "))

s=0
for i in range(1,n+1):
    s+=i

print( "Sum = ", s)
