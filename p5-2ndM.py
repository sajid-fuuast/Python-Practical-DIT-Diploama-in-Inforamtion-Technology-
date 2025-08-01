
#5.	Write a script to find all occurrences of “Baqir” in a given string ignoring the case.
#inputString = "Baqir is student of python programming class. Baqir belongs to district peshawar"


inputString = "Baqir is student of python programming class. Baqir belongs to district peshawar. baqir  "


Nos_of_occur= inputString.lower().count('baqir')


print("Occurrences of 'Baqir':", Nos_of_occur)
