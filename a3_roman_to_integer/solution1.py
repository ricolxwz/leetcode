class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        flag = ""
        for i in range(len(s)):
            if (flag == "I" and (s[i] == "V" or s[i] == "X")) or \
               (flag == "X" and (s[i] == "L" or s[i] == "C")) or \
               (flag == "C" and (s[i] == "D" or s[i] == "M")):
                total = total - 2 * dict[flag] + dict[s[i]]
            else:
                total += dict[s[i]]
            flag = s[i]
        return total
