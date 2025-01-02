from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]):
        myList = []
        indices = []
        for i in range(len(mat)):
            myList.append(mat[i][i])
            indices.append(([i],[i]))
        for i in range(len(mat)):
            if ([i],[len(mat)-i-1]) not in indices:
                myList.append(mat[i][len(mat)-i-1])
                
        total = 0
        for l in myList:
            total += l
        return total
                
s = Solution()
print(s.diagonalSum([[1,2,3],
              [4,5,6],
              [7,8,9]]))
            