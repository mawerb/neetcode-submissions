class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        newArr = [(position[i], speed[i]) for i in range(len(position))]
        newArr.sort()

        stack = []
        res = len(position)

        for i, (pos, speed) in enumerate(newArr):
            eta = (target - pos) / speed
            while stack and stack[-1] <= eta:
                stack.pop()

            stack.append(eta)
            

        return len(stack)