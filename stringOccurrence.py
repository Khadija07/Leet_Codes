class Solution(object):
    def strStr(self, haystack, needle):
        
        # pos = haystack.find(needle)
        # pos = haystack.find(needle,pos + 1)  #to check for second occurence
        # print(pos)
       
        if needle in haystack:
            return haystack.find(needle)   #returns index of first occurence of the string needle in haystack

        else:
            return -1
        
s = Solution()
print(s.strStr("LeetcodeLeeto", "Leeo"))
        