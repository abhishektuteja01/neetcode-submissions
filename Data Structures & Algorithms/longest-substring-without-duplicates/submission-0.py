class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0,1
        res = 0
        reslist = set()
        for j in range(len(s)):
            while s[j] in reslist:
                reslist.remove(s[i])
                i += 1
            reslist.add(s[j])
            res = max(res,j-i+1)
        return res


            
            

            
        