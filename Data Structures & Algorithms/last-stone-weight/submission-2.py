class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:


        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        heapq.heapify(stones)


        while len(stones) > 1:
            stoneA = heapq.heappop(stones)
            stoneB = heapq.heappop(stones)

            if stoneA < stoneB:
                heapq.heappush(stones, (stoneA-stoneB))
            elif stoneB < stoneA:
                heapq.heappush(stones, (stoneB-stoneA))

        if not stones:
            return 0
        return stones[0] * -1



