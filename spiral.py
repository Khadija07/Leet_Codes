from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]):
        myList = []
        x = 0
        while(len(myList) < (len(matrix)*len(matrix[0]))):
            
            for i in range(x, len(matrix[0])-x):    #checks left to right
                myList.append(matrix[x][i])
                #print("1",myList)
            
            for j in range(x+1,len(matrix)-x):      #checks top to bottom
                myList.append(matrix[j][i])         #the last index value remains same as previous, i
                #print("2",myList)
                
            if (len(myList) < (len(matrix)*len(matrix[0]))):      #checks right to left
                for k in range((len(matrix[0])-x-2) , x-1, -1):
                    myList.append(matrix[j][k])
                #print("3",myList)
                
                for l in range((len(matrix)-x-2) , x, -1):       #check bottom to left
                
                    myList.append(matrix[l][k])
                #print("4",myList)
            
            x += 1  #after one spiral, then we move inwards by 1 and repeat.
        
        return(myList)
        
        
            
        
    
s = Solution()
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
            
        