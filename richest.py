from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]):
        max = -1000
        for a in accounts:
            sum = 0
            for i in a:
                sum += i
            if max < sum:
                max = sum
        return max
        
            
s = Solution()
print(s.maximumWealth([[1,5],[7,3],[3,5]]))
            
        
        