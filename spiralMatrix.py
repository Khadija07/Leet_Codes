from typing import List

class Solution:
    def generateMatrix(self, n: int):
        myList = []
        matrix = []
        x = 0
        count = 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        while(count <= (n*n)):
            
            for i in range(x, n-x):    #checks left to right
                matrix[x][i] = count
                count += 1
                #print("1",matrix)
            
            for j in range(x+1,n-x):      #checks top to bottom
                matrix[j][i] = count       #the last index value remains same as previous, i
                count += 1
                #print("2",matrix)
                
            if (count <= (n*n)):      #checks right to left
                for k in range((n-x-2) , x-1, -1):
                    matrix[j][k] = count
                    count += 1
                #print("3",matrix)
                
                for l in range((n-x-2) , x, -1):       #check bottom to left
                    matrix[l][k] = count
                    count += 1
                    #print("4",matrix)
            
            x += 1  #after one spiral, then we move inwards by 1 and repeat.
        
        return(matrix)
        
        
            
        
    
s = Solution()
print(s.generateMatrix(3))
            
        