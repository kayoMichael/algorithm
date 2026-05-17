class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_mapping = {")":"(", "}": "{", "]": "["}
        for i in range(len(s)):
            if s[i] not in open_mapping:
                stack.append(s[i])
            else:
                close = open_mapping[s[i]]
                if not stack:
                    return False
                open = stack.pop()

                if open != close:
                    return False


        return len(stack) == 0
            