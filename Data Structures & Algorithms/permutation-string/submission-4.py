class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1dict = defaultdict(set)
        for s in s1:
            s1dict[s] = 1 + s1dict.get(s,0)
        i,j = 0,0
        s2dict = defaultdict(set)
        for j in range(len(s1)):
            s2dict[s2[j]] = 1 + s2dict.get(s2[j],0) 
        if s2dict == s1dict:
            return True 
        while j<len(s2)-1:
            s2dict[s2[i]] = s2dict.get(s2[i],1) - 1
            if s2dict[s2[i]] == 0:
                del s2dict[s2[i]]
            i+=1
            j+=1
            s2dict[s2[j]] = 1 + s2dict.get(s2[j],0)
            if s2dict == s1dict:
                return True 
            
        return False


        
            
            