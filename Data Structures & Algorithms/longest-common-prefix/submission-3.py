class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float('inf')
        res = strs[0]

        for string in strs[1::]:
            min_len = min(min_len, len(string))
            if len(res) > len(string):
                res = res[:len(string)]
            for i in range(min(min_len, len(res))):

                if res[i] != string[i]:
                    res = res[:i]
                    break
        
        return res