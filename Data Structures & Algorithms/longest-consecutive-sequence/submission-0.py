class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        search = []
        
        lookup = set(nums)
        res = 0

        for num in nums:
            if num-1 not in lookup and num in lookup:
                curr = num
                count = 1
                lookup.remove(curr)
                while curr + 1 in lookup:
                    if curr + 1 in lookup:
                        count += 1
                        curr += 1
                curr = num
                while curr - 1 in lookup:
                    if curr - 1 in lookup:
                        count += 1
                        curr -= 1
                if count > res:
                    res = count
        return res
