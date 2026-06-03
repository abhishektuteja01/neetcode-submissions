class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        resdict = defaultdict(set)
        windowl,i,j = 1,0,0

        for j in range(0,len(s)):
            resdict[s[j]] = resdict.get(s[j],0) + 1
            while (j-i+1) - max(resdict.values()) > k:
                resdict[s[i]] -= 1
                i+=1
            windowl = max(windowl,j-i+1)
        return windowl

                
                
        