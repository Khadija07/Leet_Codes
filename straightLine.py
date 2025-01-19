from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]):
        
        x = -1
        
        for i in range(len(coordinates)-1):
            
            y2 = coordinates[i+1][1]
            y1 = coordinates[i][1]
            x2 = coordinates[i+1][0]
            x1 = coordinates[i][0]
            
            #print(x1,x2)
        
            if((x2-x1) != 0):
                m = (y2-y1)/(x2-x1)
        
                c = y2 - (m*x2)
                
                x = 0
                
                break
        
        #print(m,x,c)
        if x == 0:
        
            for i in range(len(coordinates)):
                y = (m*coordinates[i][0]) + c
            
                if y == coordinates[i][1]:  #checking if the value of the equation matches, if yes, they are on same line
                    continue
                else:
                    return False
                        
            return True 
        return True  #this means all value of m are undefined, so points are on straight line
    
s = Solution()
print(s.checkStraightLine([[2,0],[2,1],[0,1]]))
# print(s.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
# print(s.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
# print(s.checkStraightLine([[2,0],[2,1],[0,1]]))
        
            

        