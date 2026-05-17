class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        long = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in s:
                curr = nums[i] + 1
                count = 1
                while curr in s:
                    curr += 1
                    count += 1

                long = max(long, count)

        return long

                