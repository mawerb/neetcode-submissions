class Solution:
    def tribonacci(self, n: int) -> int:
        trib_map = { 0 : 0 , 1:1, 2:1}

        for i in range(3,n+1):
            trib_map[i] = trib_map[i-1] + trib_map[i-2] + trib_map[i-3]

        return trib_map[n]
