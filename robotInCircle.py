class Solution:
    def isRobotBounded(self, instructions: str):
        robot_x = 0
        robot_y = 0
        position = 'N'
        for i in instructions:
            #print(i,position)
            if i == 'G' and position == 'N':
                robot_y += 1
            elif i == 'G' and position == 'S':
                robot_y -= 1
            elif i == 'G' and position == 'W':
                robot_x -= 1
            elif i == 'G' and position == 'E':
                robot_x += 1
            elif i == 'L' and position == 'N':
                position = 'W'
            elif i == 'L' and position == 'W':
                position = 'S'
            elif i == 'L' and position == 'S':
                position = 'E'
            elif i == 'L' and position == 'E':
                position = 'N'
            elif i == 'R' and position == 'N':
                position = 'E'
            elif i == 'R' and position == 'E':
                position = 'S'
            elif i == 'R' and position == 'S':
                position = 'W'
            elif i == 'R' and position == 'W':
                position = 'N'
            #print(robot_x,robot_y)
        
                
        
        if robot_x == robot_y == 0 or position != 'N':
            return True
        return False
    
s = Solution()
print(s.isRobotBounded("GL"))
                
                
                
                
                
            
                
                
            