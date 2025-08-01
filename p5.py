
#5.	Write a script to find all occurrences of “Baqir” in a given string ignoring the case.
#inputString = "Baqir is student of python programming class. Baqir belongs to district peshawar"


import re

inputString = "Baqir is student of python programming class. Baqir belongs to district peshawar. baqir baqir   "

Nos_of_occur = re.findall('baqir', inputString, re.IGNORECASE)


print("Occurrences of 'Baqir':", len(Nos_of_occur))
