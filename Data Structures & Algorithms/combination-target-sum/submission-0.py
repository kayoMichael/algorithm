class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def backtrack(curr, index):
            curr_sum = sum(curr) 
            if curr_sum == target:
                output.append(curr[:])
                return

            elif curr_sum > target:
                return


            for i in range(index, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i)
                curr.pop()

        backtrack([], 0)

        return output



