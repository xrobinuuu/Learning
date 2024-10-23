class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I": 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
        convert_int, offset, length, length_1 = 0, 0, len(s), len(s) - 1
        while offset < length:
            if (offset < length_1) and (roman_map[s[offset]] < roman_map[s[offset + 1]]):
                convert_int += roman_map[s[offset + 1]] - roman_map[s[offset]]
                offset += 2
            else:
                convert_int += roman_map[s[offset]]
                offset += 1
        return convert_int

    def romanToInt2(self, s: str) -> int:
        roman_map = {
            "I": 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90,
            "CD": 400, "CM": 900,
        }
        convert_int, offset, length = 0, 0, len(s)
        length_1 = length - 1
        while offset < length:
            if (offset < length_1) and (roman_map[s[offset]] < roman_map[s[offset + 1]]):
                convert_int += roman_map[s[offset: offset + 2]]
                offset += 2
            else:
                convert_int += roman_map[s[offset]]
                offset += 1
        return convert_int


if __name__ == '__main__':
    _s = "MCMXCIV"
    result = Solution().romanToInt(_s)
    print(result)
