class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1dict = defaultdict(int)
        for s in s1:
            s1dict[s] +=1
        s2dict = defaultdict(int)
        for j in range(len(s1)):
            s2dict[s2[j]] +=1 
        if s2dict == s1dict:
            return True 
        i=0
        for j in range(len(s1), len(s2)):
            s2dict[s2[i]] -= 1
            if s2dict[s2[i]] == 0:
                del s2dict[s2[i]]
            i+=1
            s2dict[s2[j]] += 1
            if s2dict == s1dict:
                return True  
        return False


        
            
            