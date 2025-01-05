from typing import List

class Solution:
    def hasTrailingZeros(self, nums: List[int]):
        totalList = []
     
        
        for n in nums:
            N = n
            myList = []
            while(N >= 1):              #decimal to binary
                myList.append(N % 2)
                N = N // 2
            myList.reverse()
            #print(n, myList)
            totalList.append(myList)
            
        if len(totalList) == 2:
            zero = totalList[1][len(totalList[1])-1] + totalList[0][len(totalList[0])-1]
            if zero == 0:
                return True
            
            return False
        
        else:
            
            for i in range(len(totalList)):
                for j in range(i+1,len(totalList)):
                    zero = totalList[j][len(totalList[j])-1] + totalList[i][len(totalList[i])-1]
                    #print(totalList[i],totalList[j],zero)
                    if zero == 0:
                        return True
            
            return False
        
                
                    
            
                
        
s = Solution()
print(s.hasTrailingZeros([33,40,84]))