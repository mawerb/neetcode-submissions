class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = {}
        res = ""

        for i in range(len(s)):
            si = str(i)

            l,r = i, i+1
            curr = s[i]

            while l >= 0 and r < len(s):
                
                if s[l] == s[r]:
                    curr = s[l:r+1]
                    l-=1
                    r+=1

                else: 
                    break

            if len(curr) > len(res):
                print(i)
                res = curr

            l,r = i, i
            curr = s[i]

            while l >= 0 and r < len(s):
                
                if s[l] == s[r]:
                    curr = s[l:r+1]
                    l-=1
                    r+=1
                else: 
                    break

            if len(curr) > len(res):
                print(i)
                res = curr

        return res


        


            