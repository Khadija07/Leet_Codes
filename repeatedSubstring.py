class Solution(object):
    def repeatedSubstringPattern(self, s):
        
        l = int(len(s) / 2)
                
        
        for i in range(1,l+1):
            sub = s[0:i]
            #print(sub)
            check_length = (len(s) - len(sub))/len(sub)  #the number of occurances a substring should have in a string(s) 
            #print("check",check_length)
            pos = s.find(sub)
            count = -1
            while pos != -1:
                count += 1 #calculates number of occurances
                pos = s.find(sub, pos+len(sub))
                #print("pos",pos)
                
            #print(count)
                
            if count != check_length: #checks the actual occurance with the expected
                continue
            else:
                return True
            
        return False
            
                    
s = Solution()
#print(s.repeatedSubstringPattern("babbabbabbabbabbabbab"))
print(s.repeatedSubstringPattern("aabaaba"))