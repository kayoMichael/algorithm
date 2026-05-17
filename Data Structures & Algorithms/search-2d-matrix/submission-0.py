class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (right + left) // 2

            l, r = matrix[mid][0], matrix[mid][-1]

            if l <= target and r >= target:
                lst = matrix[mid]
                l2 = 0
                r2 = len(matrix[0]) - 1

                while l2 < r2:
                    mid = (l2 + r2) // 2

                    if lst[mid] < target:
                        l2 = mid + 1 

                    else:
                        r2 = mid

                return lst[l2] == target

            
            if target < l:
                right = mid -1

            else:
                left = mid + 1

        
        return False