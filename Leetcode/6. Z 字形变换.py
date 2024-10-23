from itertools import chain


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        step = numRows * 2 - 2
        if length <= numRows or numRows == 1:
            return s
        converted = []
        for i in range(0, step):
            div, mod = divmod(i, numRows)
            row = div + mod + 1 if div % 2 == 0 else numRows - mod - 1
            sub_convert = [s[i] for i in range(i, length, step)]
            if row > len(converted):
                converted.append(sub_convert)
            else:
                begin = converted[row - 1]
                sub_convert.extend([''] * (len(begin) - len(sub_convert)))
                converted[row - 1] = sum(list(zip(begin, sub_convert)), ())
        return "".join(chain(*converted))

    def convert2(self, s: str, numRows: int) -> str:
        length = len(s)
        step = numRows * 2 - 2
        if length <= numRows or numRows == 1:
            return s
        converted = []
        for i in range(0, step):
            div, mod = divmod(i, numRows)
            row = div + mod + 1 if div % 2 == 0 else numRows - mod - 1
            sub_convert = ''.join([s[i] for i in range(i, length, step)])

            if row > len(converted):
                converted.append(sub_convert)
            else:
                begin = converted[row - 1]
                sub_convert = sub_convert.ljust(len(begin), ' ')
                converted[row - 1] = ''.join(chain(*zip(begin, sub_convert))).replace(' ', '')
        return "".join(converted)

    def convert3(self, s: str, numRows: int) -> str:
        length = len(s)
        if length <= numRows or numRows == 1:
            return s

        step = numRows * 2 - 2
        converted = [''] * numRows
        for i in range(0, length):
            mod = i % step
            converted[numRows - (mod % numRows) - 2 if mod >= numRows else (mod % numRows)] += s[i]
        return ''.join(converted)

    def convert4(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        step = 2 * numRows - 2
        indexed_s = list(enumerate(s))
        indexed_s.sort(key=lambda x: (x[0] % step) if (x[0] % step) < numRows else (step - x[0] % step))
        return ''.join([char for _, char in indexed_s])


if __name__ == '__main__':
    _s = "PAYPALISHIRING"
    _numRows = 4
    result = Solution().convert4(_s, _numRows)
    print(result)
    target = "PINALSIGYAHRPI"
    print(result == target)
