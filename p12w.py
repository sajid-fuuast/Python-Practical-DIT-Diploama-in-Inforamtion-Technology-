#12.	Write a script to calculate the sum of all numbers
# from 1 to a given number (while, for).



n=int(input("Enter Numbere :"))

s=0
i=1

while i<=n:
    s=s+i   # s+=i
    i+=1   # i=i+1

print("Sum is  ", s)
