class Solution:
    def lengthOfLastWord(self, s: str):
        
        words = s.split()
        l = len(words) - 1
        return len(words[l])
    
s = Solution()
print(s.lengthOfLastWord('  luffy is  still    joyboy'))