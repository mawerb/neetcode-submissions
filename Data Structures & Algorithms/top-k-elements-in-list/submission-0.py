# array of ints (nums), int k

# output : array[int] (representing the k most frequent elements within the array)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import defaultdict

        numCountArr = []
        numCounter = defaultdict(int)


        for num in nums:
            numCounter[num] += 1
            
            if len(numCountArr) < numCounter[num]:
                numCountArr.append(set())

            numCountArr[numCounter[num] - 1].add(num)
            if (numCounter[num] != 1):
                numCountArr[numCounter[num] - 2].remove(num)

        res = []

        while k > 0:
            curr = numCountArr[-1]
            k -= len(curr)

            res += list(numCountArr.pop())
        
        return res