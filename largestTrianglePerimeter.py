from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]):
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            
            a = nums[i]
            b = nums[i+1]
            c = nums[i+2]
            
            #triangle can only exist if the sum of the lengths of any two sides is greater than the length of the third side
            cond1 = True if ((a+b) > c) else False
            cond2 = True if ((a+c) > b) else False
            cond3 = True if ((c+b) > a) else False
            
            if cond1 == cond2 == cond3 == True:
                return (a+b+c)
        return (0)
            
                
        
            
s = Solution()
print(s.largestPerimeter([1,2,1,10]))
            
            
        