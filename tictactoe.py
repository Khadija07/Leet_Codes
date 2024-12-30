from typing import List
class Solution:
    def tictactoe(self, moves: List[List[int]]):
        game = [ [0]*3 for i in range(3)]
        count = 0
        for m in moves:
            if count == 0:
                game[m[0]][m[1]] = 'X'
                count = 1
            elif count == 1:
                game[m[0]][m[1]] = 'O'
                count = 0
                

        print(game)
        
        if ((game[0][0] == game[0][1] == game[0][2] == 'X') or (game[1][0] == game[1][1] == game[1][2] == 'X') or (game[2][0] == game[2][1] == game[2][2] == 'X')):
            return 'A'
        if ((game[0][0] == game[1][0] == game[2][0] == 'X') or (game[0][1] == game[1][1] == game[2][1] == 'X') or (game[0][2] == game[1][2] == game[2][2]  == 'X')):
            return 'A'
        if ((game[0][0] == game[1][1] == game[2][2] == 'X') or (game[0][2] == game[1][1] == game[2][0] == 'X')):
            return 'A'
        if ((game[0][0] == game[0][1] == game[0][2] == 'O') or (game[1][0] == game[1][1] == game[1][2] == 'O') or (game[2][0] == game[2][1] == game[2][2] == 'O')):
            return 'B'
        if ((game[0][0] == game[1][0] == game[2][0] == 'O') or (game[0][1] == game[1][1] == game[2][1] == 'O') or (game[0][2] == game[1][2] == game[2][2] == 'O')):
            return 'B'
        if ((game[0][0] == game[1][1] == game[2][2] == 'O') or (game[0][2] == game[1][1] == game[2][0] == 'O')):
            return 'B'
        if any(0 in row for row in game): 
            return 'Pending'
        else:
            return 'Draw'
            
s = Solution()
print(s.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2]]))