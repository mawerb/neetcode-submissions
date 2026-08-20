class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        num_len = len(nums)/2
        for num in nums:
            count[num] += 1

            if count[num] > num_len:
                return num
                
        