from typing import List

class Solution:
    def arraySign(self, nums: List[int]):
        total = 1
    
        for i in range(len(nums)):
            total = total * nums[i]
            
        if total > 0:
            return 1
        elif total < 0:
            return -1
        else:
            return 0
                
s = Solution()
print(s.arraySign([-1,-1,-1,-1,-1]))