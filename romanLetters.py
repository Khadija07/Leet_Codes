class Solution:
    def romanToInt(self, s: str):
        total = 0
        if s == 'IV' or 'IV' in s:
            s = s.replace('IV','')
            total += 4
        if s == 'IX' or 'IX' in s:
            s = s.replace('IX','')
            total += 9
        if s == 'XL' or 'XL' in s:
            s = s.replace('XL','')
            total += 40
        if s == 'XC' or 'XC' in s:
            s = s.replace('XC','')
            total += 90
        if s == 'CD' or 'CD' in s:
            s = s.replace('CD','')
            total += 400
        if s == 'CM' or 'CM' in s:
            s = s.replace('CM','')
            total += 900
        
        if (len(s) != 0):
            
            for i in range(len(s)):
                if s[i] == 'I':
                    total += 1
                if s[i] == 'V':
                    total += 5
                if s[i] == 'X':
                    total += 10
                if s[i] == 'L':
                    total += 50
                if s[i] == 'C':
                    total += 100
                if s[i] == 'D':
                    total += 500
                if s[i] == 'M':
                    total += 1000
            
        return total
                    
        
s = Solution()
print(s.romanToInt('MCMXCIV'))