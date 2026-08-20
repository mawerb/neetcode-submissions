class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        max_avg = sum(matchsticks) / 4

        if max_avg % 1 != 0:
            return False


        matchsticks.sort(reverse=True)

        if matchsticks[0] > max_avg:
            return False

        sides = [0,0,0,0]
        count = 0

        def backtrack(i):
            if i == len(matchsticks):
                return all(side == max_avg for side in sides)
            
            for side in range(4):
                stick = matchsticks[i]

                if sides[side] + stick > max_avg:
                    continue
                
                sides[side] += stick

                if backtrack(i+1):
                    return True
                
                sides[side] -= stick

                if sides[side] == 0:
                    break

            return False

        return backtrack(0)




            
