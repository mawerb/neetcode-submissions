class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(number: int) -> int:
            res = 0

            while number != 0:
                if (number & 1) == 1:
                    res += 1
                number = (number >> 1)
            return res

        ret = []

        for i in range(n+1):
            ret.append(count(i))

        return ret
        