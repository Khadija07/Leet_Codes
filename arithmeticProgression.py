from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]):
        
        arr.sort()
        diff = arr[1] - arr[0]
        i = 2
        count = 0
        while(i < len(arr)):
            diff_elements = arr[i] - arr[i-1]
            #print(diff_elements)
            if (diff_elements == diff):
                count += 1 
            i += 1
                
        if count == (len(arr) - 2):
            return True
        return False
    
s = Solution()
print(s.canMakeArithmeticProgression([1,2,4]))
        
        
# A sequence of numbers is called an arithmetic 
# progression if the difference between any two consecutive elements is the same.