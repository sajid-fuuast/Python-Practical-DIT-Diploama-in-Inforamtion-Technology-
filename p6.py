
#6.	Write a script to split a given string on hyphens and display each substring.
# inputString = Bareera-is-a-data-scientist


inputString = "Bareera-is-a-data-scientist"


substrings = inputString.split('-')

#print(" ".join(substrings))

for i in substrings:
    print(i)
