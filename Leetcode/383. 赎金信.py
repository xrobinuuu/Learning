class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        tmp = set(ransomNote)
        for i in tmp:
            # if ransomNote.count(i) > magazine.count(i):
            #     return False
            pass
        else:
            return True


_ransomNote = "c"
_magazine = "aab"
result = Solution().canConstruct(_ransomNote, _magazine)
print(result)
