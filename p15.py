#15.	Write a script that takes five fruits name from the user and store it in a list.
# Display the list elements using for loop.
fruits = []

for i in range(5):
    fr= input(f"Enter the name of fruit {i + 1}: ")
    fruits.append(fr)

print("\nList of Fruits:")
for f in fruits:
    print(f)



