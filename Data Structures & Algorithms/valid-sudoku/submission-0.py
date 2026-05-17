class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                if num == ".":
                    continue

                if num in valid[r]:
                    return False

                if num in valid[c + 9]:
                    return False

                if num in valid[(r // 3) * 3 + (c // 3) + 18]:
                    return False

                valid[r].add(num)
                valid[c + 9].add(num)
                valid[(r // 3) * 3 + (c // 3) + 18].add(num)


        return True