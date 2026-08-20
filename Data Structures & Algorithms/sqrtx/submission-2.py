class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x

        while (end - start) > 1:
            midpt = start + (end - start) // 2
            curr = midpt*midpt

            if curr == x:
                return midpt
            elif curr > x:
                end = midpt
            else:
                start = midpt
        
        if end * end <= x:
            return end
        return start
            
        