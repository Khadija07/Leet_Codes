
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]):
        
        i = 0
        my_list = []
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                my_list.append(0)
            else:
                i += 1   #incrementing when value is not 0, else the nums[i] will become out of range
                
        nums.extend(my_list)
        print(f"[{','.join(map(str, nums))}]")
    
    
s = Solution()
#s.moveZeroes([0,1,0,3,12])
s.moveZeroes([0,1,0,0,12,5,6])


        
        