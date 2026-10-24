class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        seen = set(s[0])
        res = 1
        l = 0


        for i in range(1, len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[i])
            res = max(len(seen), res)

        return res