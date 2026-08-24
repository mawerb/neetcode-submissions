class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = {}

        def dfs(start, end):
            if (start,end) in dp:
                return dp[(start,end)]
            elif start == len(s):
                dp[(start,end)] = True
                return True
            elif end == len(s) + 1:
                dp[(start,end)] = False
                return False

            word = s[start:end]

            if word in wordDict:
                take = dfs(end, end + 1)
            else:
                take = False
            skip = dfs(start, end+1)

            dp[(start,end)] = skip or take
            return take or skip
        
        return dfs(0,1)

