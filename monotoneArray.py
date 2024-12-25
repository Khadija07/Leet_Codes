from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        new_list = nums[:]
        
        new_list.sort()
        
        if new_list == nums:
            return True
        else:
            new_list.sort(reverse=True)
            if new_list == nums:
                return True
                
            return False
        
s = Solution()
print(s.isMonotonic([5,4,3,2,1]))