class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = (right + left) // 2
            
            count = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    count += 1

            if count > mid:
                right = mid

            else:
                left = mid + 1

        return left

            


