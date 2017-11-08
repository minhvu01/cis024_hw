def sortAcsending(myList):
   ''' sort ascending order '''
   sortedList = []
   if len(myList) < 2:
      sortedList = myList
   else:
      while myList:
         minNum = min(myList)
         myList.remove(minNum)
         sortedList.append(minNum)
   return sortedList

def sortDecending(myList):
   ''' sort decending order '''
   sortedList = []
   if len(myList) < 2:
      sortedList = myList
   else:
      while myList:
         maxNum = max(myList)
         myList.remove(maxNum)
         sortedList.append(maxNum)
   return sortedList
