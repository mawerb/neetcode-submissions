class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_seen = set()
        multi_seen = set()

        for n in nums:
            if n in single_seen:
                single_seen.remove(n)
                multi_seen.add(n)
            else:
                single_seen.add(n)

        return single_seen.pop()