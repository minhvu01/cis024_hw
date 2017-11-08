
from sorthelper import sortAcsending

import sys

#print(sys.argv, len(sys.argv))

inputList = []
# get all args put in a list
for i in range(1,len(sys.argv)):
   inputList.append(sys.argv[i]) 

print("Original  list: ", inputList)
print("Sort acsending: ", sortAcsending(inputList))
