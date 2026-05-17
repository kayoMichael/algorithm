class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (right + left) // 2

            if nums[mid] > nums[right]:
                if target <= nums[mid] and target >= nums[left]:
                    right = mid

                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                else:
                    right = mid

        return left if nums[left] == target else -1
