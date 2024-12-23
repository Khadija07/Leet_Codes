#checking t is anagram of s
class Solution(object):
    def isAnagram(self, s, t):
        
        s_sort = ''.join(sorted(s))
        t_sort = ''.join(sorted(t))
        
        if s_sort == t_sort:
            return "true"
        else:
            return "false"
            
s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))
        