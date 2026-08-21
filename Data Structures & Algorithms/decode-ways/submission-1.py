class Solution:
    def numDecodings(self, s: str) -> int:

        import string

        strings={letter:i for letter,i in enumerate(string.ascii_lowercase, start=1)}

        res=0
        dp = {}

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if str(i) in dp:
                return dp[str(i)]

            res = dfs(i+1)

            if i+1 < len(s) and int(s[i:i+2]) < 27:
                res += dfs(i+2)
            
            dp[str(i)] = res

            return res

        return dfs(0)


