class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_val = 0
        total_cap = 0

        for weight in weights:
            max_val = max(weight, max_val)
            total_cap += weight

        start = max_val
        end = total_cap

        def day_count(capacity):
            r = 0
            running_cap = 0
            days=0
            while r<len(weights):
                running_cap += weights[r]
                if running_cap == capacity:
                    running_cap = 0
                    days += 1
                elif running_cap > capacity:
                    running_cap = weights[r]
                    days += 1
                r += 1
            if running_cap == 0:
                return days
            return days + 1
                
        min_capacity = float('inf')
        while end - start >= 0:
            midpt = start + (end - start) // 2
            if day_count(midpt) > days:
                start = midpt + 1
                continue
            
            min_capacity = midpt
            end = midpt - 1
        
        return min_capacity