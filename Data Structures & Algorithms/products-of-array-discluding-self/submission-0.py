class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] * len(nums)
        r = [1] * len(nums)


        for i in range(len(nums)):
            prev = l[i]

            if i != 0:
                prev = l[i-1]
            
            l[i] *= prev * nums[i]

        for j in range(len(nums)-1, -1, -1):
            prev = r[j]

            if j != len(nums) - 1:
                prev = r[j+1]
            
            r[j] *= prev * nums[j]

        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(r[i+1])
            elif i == len(nums)-1:
                res.append(l[i-1])
            else:
                res.append(l[i-1] * r[i+1])

        return res
        