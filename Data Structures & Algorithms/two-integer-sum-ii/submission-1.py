class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            curr = numbers[i]
            diff = target - curr
            j = i + 1

            while j != len(numbers) and diff - numbers[j] >= 0:
                if diff - numbers[j] == 0:
                    return [i+1,j+1]
                j += 1

