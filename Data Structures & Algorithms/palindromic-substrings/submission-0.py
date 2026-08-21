class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def search_palindrome(l,r):
            if l < 0 or r == len(s):
                return 0 
            
            if s[l] == s[r]:
                return 1 + search_palindrome(l-1,r+1)
            else:
                return 0

        for i in range(len(s)):
            res += search_palindrome(i,i+1)
            res += search_palindrome(i,i)

        return res