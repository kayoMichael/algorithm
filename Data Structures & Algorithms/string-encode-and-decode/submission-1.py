class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for word in strs:
            output.append(f"{len(word)}#{word}")

        return ''.join(output)

    def decode(self, s: str) -> List[str]:
        output = []
        index = 0
        while index < len(s):
            count = 0
            while s[index] != "#":
                count = count * 10 + int(s[index])
                index += 1
            word = []
            index += 1
            while count > 0:
                word.append(s[index])
                count -= 1
                index += 1

            output.append(
                "".join(word)
            )

        return output

