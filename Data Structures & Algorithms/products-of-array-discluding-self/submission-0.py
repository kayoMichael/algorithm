class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = [1]

        for i in range(len(nums) - 1, 0, -1):
            suffix.append(suffix[-1] * nums[i])

        prefix = 1
        output = []
        index = len(suffix) - 1
        for i in range(len(nums)):
            output.append(prefix * suffix[index])
            index -= 1
            prefix *= nums[i]

        return output

        

