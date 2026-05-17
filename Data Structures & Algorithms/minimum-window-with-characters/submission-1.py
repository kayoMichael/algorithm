class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = Counter(t)
        left = 0
        total = (float("inf"), [])
        length = len(freq)
        for right in range(len(s)):
            if s[right] in freq:
                freq[s[right]] -= 1

                if freq[s[right]] == 0:
                    length -= 1

            while length == 0:
                if right - left + 1 < total[0]:
                    total = (right - left + 1, s[left: right + 1])

                if s[left] in freq:
                    freq[s[left]] += 1
                    if freq[s[left]] > 0:
                        length += 1

                left += 1


        return "".join(total[1])

            

                


