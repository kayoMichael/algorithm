class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        value = sorted(zip(position, speed))

        current_fleet = 0
        for i in range(len(value) - 1, -1, -1):
            pos, speed = value[i]
            t = (target - pos) / speed 
            if t > current_fleet:
                current_fleet = t

                fleet += 1

        return fleet