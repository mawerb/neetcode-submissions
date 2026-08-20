class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        newArr = [0] * (len(cost) + 1)

        for i in range(2,len(cost) + 1):
            newArr[i] = min(newArr[i-1] + cost[i-1], newArr[i-2] + cost[i-2])
        

        return newArr[-1]

