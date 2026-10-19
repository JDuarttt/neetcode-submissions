class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(len(t)>len(s)): return ""
        mapT = {}
        mapCount = {}
        for c in t:
            mapT[c] = mapT.get(c, 0) +1
            mapCount[c] = 0
        l = 0
        minLen = float('inf')
        minString = ""
        while(l<len(s) and (not s[l] in mapT)):
            l+=1
        if(l >= len(s)): return ""
        mapCount[s[l]]=1
        if(mapT == mapCount):
            return s[l:l+1]
        r = l+1
        while(r<len(s)):
            if(s[r] in mapT):
                mapCount[s[r]] = mapCount.get(s[r],0)+1
                if(s[r] == s[l] and mapCount[s[l]] > mapT[s[l]]):
                    while((not (s[l] in mapT)) or (mapCount[s[l]] > mapT[s[l]])):
                        if(s[l] in mapT):
                            mapCount[s[l]]-=1
                        l+=1
            is_valid=True
            for key in mapT:
                if(mapCount.get(key,0) < mapT[key]):
                    is_valid = False
                    break
            if(is_valid):
                if(r-l+1< minLen):
                    minLen = r-l+1
                    minString = s[l:r+1]
                    if(len(minString) == len(t)):
                        return minString
            r+=1
        return minString