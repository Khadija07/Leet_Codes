
class Solution:
    def judgeCircle(self, moves: str):
        robot_x = 0
        robot_y = 0
        for m in moves:
            if m == 'U':
                robot_y += 1
            if m == 'D':
                robot_y -= 1
            if m == 'L':
                robot_x -= 1
            if m == 'R':
                robot_x += 1
                
        if robot_x == 0 and robot_y == 0:
            return True
        return False        
        
s = Solution()
print(s.judgeCircle("LL"))
        