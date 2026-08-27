class Solution:
    def reverseBits(self, n: int) -> int:

        i = 0
        bits = []

        while n != 0:
            if (n & 1):
                bits.append(1)
            else:
                bits.append(0)
            
            n = n >> 1

        res = 0
        N = len(bits)

        while bits:
            if bits.pop(0):
                res = res | 1
            if bits:
                res = res << 1

        for i in range(32-N):
            res = res << 1

        return res
