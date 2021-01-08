class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        rev_x = ''
        if str_x[0] == '-':
            str_x = str_x[1:]
            rev_x = '-'

        for d in str_x[::-1]:
            rev_x += d

        rev_x = int(rev_x)
        if rev_x > 2 ** 31 - 1 or rev_x < -2 ** 31:
            return 0
        else:
            return rev_x