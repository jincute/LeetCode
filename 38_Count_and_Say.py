class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        ini = "1"
        i = 1
        while i < n:
            # print('i: ', i)
            # print('ini: ', ini)
            value = ini[0]
            count = 1
            new_ini = ""
            for j in ini[1:]:
                if value == j:
                    count += 1
                else:
                    # print('in')
                    new_ini += str(count)
                    new_ini += value
                    value = j
                    count = 1
                # print('new_ini: ', new_ini)
            new_ini += str(count)
            new_ini += value
            # print(new_ini)
            ini = new_ini
            i += 1
        return new_ini