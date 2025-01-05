class Solution:
    def removeTrailingZeros(self, num: str):
        if '0' in num:
            i = len(num)-1    #starting from last element
            while(i < len(num)):
                #print(i,num,num[i])
                if num[i] != '0':
                    break
                num = num[:-1]  #removes last char from string, negative indexing
                i -= 1
        return num
            
        
s = Solution()
print(s.removeTrailingZeros("1000"))
        