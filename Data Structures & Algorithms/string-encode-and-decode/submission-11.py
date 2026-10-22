class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "#"
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        def helper(s : str, sArr : List[str]) -> List[str]:
            if not s:
                return []

            count = 0
            c = s[0]
            length = ""
            i = 0

            while c != "#":
                length += s[i]

                i+=1
                c = s[i]

            sLen = int(length)
            res = ""

            for i in range(i + 1, sLen + i + 1):
                res += s[i]
            if i + 1 != len(s):
                return helper(s[i+1:], sArr + [res])

            return sArr + [res]
        return helper(s,[])

