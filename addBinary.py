class Solution:
    def addBinary(self, a: str, b: str):
        
        x = len(a) - 1
        a_dec = 0
      
        for i in a:
            A = int(i)
            value = A * pow(2,x)
            a_dec += value
            x -= 1
        
        y = len(b) - 1
        b_dec = 0
      
        for i in b:
            B = int(i)
            value = B * pow(2,y)
            b_dec += value
            y -= 1
        
        total = a_dec + b_dec
        if(total == 0):
            return ('0')
        else:
            myList = []
            while(total >= 1):              #decimal to binary
                myList.append(total % 2)
                total = total // 2
            
            myList.reverse()
            result = ''.join(str(s) for s in myList)
            return result
        
        
        
        
            
            
            
            
s = Solution()
print(s.addBinary('0','0'))
        