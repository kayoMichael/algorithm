class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = Counter(s)
        t_count = Counter(t)
        for i in range(len(s)):
            s_count[t[i]] -= 1
            t_count[s[i]] -= 1
            if s_count[t[i]] < 0 or s_count[s[i]] < 0:
                return False


        return True

