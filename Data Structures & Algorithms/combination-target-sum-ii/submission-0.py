class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()
        def backtrack(curr, index):
            summ = sum(curr)
            if summ == target:
                output.append(curr[:])
                return

            if summ > target:
                return


            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                curr.append(candidates[i])
                backtrack(curr, i + 1)
                curr.pop()

        backtrack([], 0)
        return output