class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = dict()

        for i in range(len(nums)):
            curr = nums[i]

            if curr not in hashmap:
                hashmap[curr] = i
            else:
                if abs(hashmap[curr] - i) <= k:
                    return True
                hashmap[curr] = i
            
        return False