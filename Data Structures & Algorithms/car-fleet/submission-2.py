class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        value = sorted(zip(position, speed), reverse=True)

        for i in range(len(value)):
            pos, mph = value[i]
            t = (target - pos) / mph

            if not stack or stack[-1] < t:
                stack.append(t)

        return len(stack)
    