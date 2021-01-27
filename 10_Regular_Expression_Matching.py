class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        table = [[False]*(len(p)+1) for _ in range(len(s)+1)]
#         print(table)
        table[0][0] = True
        for i in range(len(s)+1):
            for j in range(1, len(p)+1):
                first_match = i>0 and p[j-1] in (s[i-1], ".")
                if j >= 2 and p[j-1]=='*':
                    table[i][j] = table[i][j-2] or table[i-1][j] and p[j-2] in (s[i-1], ".")
                else:
                    table[i][j] = first_match and table[i-1][j-1]
        return table[len(s)][len(p)]