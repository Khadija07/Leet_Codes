from tokenize import Double
from typing import List

class Solution:
    def average(self, salary: List[int]):
        salary.sort()
        salary.remove(salary[0])
        salary.remove(salary[len(salary)-1])
        total = 0.0
        for s in salary:
            
            total += s
        avg = float(total / len(salary))
            
        print(f"{avg:.5f}")
        
s = Solution()
s.average([4000,3000,1000,2000])
        