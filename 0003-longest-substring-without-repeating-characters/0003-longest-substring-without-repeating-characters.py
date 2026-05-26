class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        

        maxi = 0
        if len(s) == 1:
            return 1


        for i in range(0,len(s)-1):
            count = 0
            seen = set()
            for j in range(i,len(s)):
                if s[j]  in seen:
                    break
                    
                    
                    
                seen.add(s[j])
                count+=1
                maxi = max(maxi,count)
        return maxi


        