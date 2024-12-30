
from typing import List

class Solution:
    def calPoints(self, operations: List[str]):
        myList = []
        
        for i in operations:
            if i == 'C':
                myList.pop()
            
            elif i == '+':
                add = 0
                
                add = int(myList[len(myList)-1]) + int(myList[len(myList)-2])
                myList.append(add)
            elif i == 'D':
                new_score = int(myList[len(myList)-1]) * 2
                myList.append(new_score)
                
            else:
                myList.append(i)
                
            
        #print(myList)
        
        total = 0
        for l in myList:
            total += int(l)
        return total
        
                

s = Solution()
print(s.calPoints(["1","C"]))