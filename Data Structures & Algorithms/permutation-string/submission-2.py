class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1 = Counter(s1)
        right = len(s1) - 1
        for left in range(len(s2) - len(s1) + 1):
            c2 = Counter(s2[left: left + len(s1)])
            if c2 == c1:
                return True

        return False

