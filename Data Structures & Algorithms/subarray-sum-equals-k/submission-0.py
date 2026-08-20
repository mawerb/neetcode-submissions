class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        prefixsum = 0
        hashmap = defaultdict(int)

        hashmap[0] = 1
        count = 0

        for num in nums:
            prefixsum += num

            count += hashmap[prefixsum-k]

            hashmap[prefixsum] += 1

        return count