class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        
        newHeap = []
        res = []

        for i in range(len(points)):
            x,y = points[i]

            dist = math.sqrt((0-x)**2 + (0-y)**2)

            heapq.heappush(newHeap,(dist, i))

        while k > 0:
            res.append(points[heapq.heappop(newHeap)[1]])
            k-=1

        return res
