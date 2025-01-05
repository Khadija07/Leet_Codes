class Solution:
    def countOdds(self, low: int, high: int):
        myList = []
        value = int((high - low) / 2)
        
            
            
       
        if (low % 2 != 0) or (high % 2 != 0):
            return (value + 1)
        return value
            
            

        # for i in range(low,high+1):
        #     if i % 2 != 0:
        #         myList.append(i)
        
        # return len(myList)
    
s = Solution()
#print(s.countOdds(21,22))
print(s.countOdds(800445804,979430543))
                
        