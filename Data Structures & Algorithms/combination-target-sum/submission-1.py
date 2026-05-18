class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def backtrack(curr, index):
            summa = sum(curr)
            if summa == target:
                output.append(curr[:])
                return

            if summa > target:
                return

            
            for i in range(index, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i)
                curr.pop()

        backtrack([], 0)
        return output