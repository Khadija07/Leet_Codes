from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]):
        myList = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if 0 == matrix[i][j]:
                    myList.append((i,j))
            
        for l in myList:
            if l[0] == 0 and l[1] == 0:
                for i in range(1,len(matrix[0])):   #top left to right
                    matrix[0][i] = 0
                for i in range(1,len(matrix)):      #top to bottom
                    matrix[i][0] = 0
                #print(matrix)
            
            elif l[0] == (len(matrix)-1) and l[1] == 0:
                for i in range(1,len(matrix[0])):     #bottom left to right
                    matrix[(len(matrix))-1][i] = 0
                for i in range((len(matrix)-1),-1,-1):  #bottom to top
                    matrix[i][0] = 0    
            
            elif l[0] == 0 and l[1] == (len(matrix[0])-1):
                for i in range((len(matrix[0])-2),-1,-1):   #top right to left
                    matrix[0][i] = 0
                for i in range(1,len(matrix)):      #top to bottom
                    matrix[i][len(matrix[0])-1] = 0
                #print(matrix)
            
            elif l[0] == (len(matrix)-1) and l[1] == (len(matrix[0])-1):
                for i in range((len(matrix[0])-2),-1,-1):     #bottom right to left
                    matrix[(len(matrix)-1)][i] = 0
                for i in range((len(matrix)-2),-1,-1):  #bottom to top
                    matrix[i][len(matrix[0])-1] = 0    
            else:
                for i in range(l[1]+1,len(matrix[0])):    #from l[0] to right
                    matrix[l[0]][i] = 0
                    #print('1',matrix)
                for i in range(l[1]-1,-1,-1):             #from l[0] to left
                    matrix[l[0]][i] = 0
                    #print('2',matrix)
                for i in range(l[0]+1,len(matrix)):       #from l[1] to bottom
                    matrix[i][l[1]] = 0
                    #print('3',matrix)
                for i in range(l[0]-1,-1,-1):             #from l[1] to top
                    matrix[i][l[1]] = 0
                    #print('4',matrix)
                
            
            
                 
        return matrix
    

s = Solution()
print(s.setZeroes([[2147483647,2,9],[2,6,7],[1,8,8],[5,0,1],[9,6,0]]))