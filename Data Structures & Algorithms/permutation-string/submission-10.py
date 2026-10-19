class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)): return False
        s1Dict, s2Dict = [0]*26, [0]*26
        for c in s1:
            s1Dict[ord(c)-97]+=1
        l,r = 0, len(s1)-1
        matches = 0
        for i in range(len(s1)):
            s2Dict[ord(s2[i])-97]+=1
        for i in range(26):
            if(s1Dict[i]==s2Dict[i]):
                matches += 1
        if(matches == 26): return True
        l+=1
        r+=1
        while(r < len(s2)):
            s2Dict[ord(s2[l-1])-97]-=1
            if(s2Dict[ord(s2[l-1])-97] == s1Dict[ord(s2[l-1])-97]): matches += 1
            elif(s2Dict[ord(s2[l-1])-97]+1 == s1Dict[ord(s2[l-1])-97]): matches -= 1
            s2Dict[ord(s2[r])-97]+=1
            if(s2Dict[ord(s2[r])-97] == s1Dict[ord(s2[r])-97]): matches += 1
            elif(s2Dict[ord(s2[r])-97]-1 == s1Dict[ord(s2[r])-97]): matches -= 1
            if(matches == 26): return True
            l+=1
            r+=1
        return False


        