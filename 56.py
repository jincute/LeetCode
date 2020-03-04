from typing import List
import pdb
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l = len(intervals)
        merge_list = []
        temp_list = []
        next_list = []
        merge_flag = False
        for i in range(l-1):
            if merge_flag == False:
                temp_list = intervals[i]
            else:
                i += 1

            if i == l-1:
                next_list = intervals[l-1]
            else:
                next_list = intervals[i+1]
            if temp_list[0] <= next_list[0]:
                if temp_list[1] <= next_list[1]:
                    temp_list[1] = next_list[1]
                    merge_flag = True
            else:
                temp_list[0] = next_list[0]
                merge_flag = True

            merge_list.append([temp_list[0],temp_list[1]])

        return merge_list
            #pdb.set_trace()

#S = Solution().merge([[1,3],[2,6],[8,10],[15,18]])
S = Solution().merge([[0, 2], [1, 4], [3, 5]])
print(S)

'''
c_l = intervals[i][0]
p_l = intervals[i-1][0]
c_r = intervals[i][1]
p_r = intervals[i-1][1]

if c_l <= p_r and c_r >= p_l:
    if c_l >= p_l and c_r >= p_r:
        temp_list.append([p_l, c_r])
    elif c_l < p_l and c_r >= p_r:
        merge_list.append([c_l, c_r])
    elif c_l < p_l and c_r <= p_r:
        merge_list.append([c_l, p_r])
    else:
        merge_list.append([p_l, p_r])
    i -= 1
    if i == 0:
        break;
else:
    if i == 1:
        merge_list.append([c_l, c_r])
        merge_list.append([p_l, p_r])
    else:
        merge_list.append([c_l, c_r])

#merge_list.append([p_l, p_r])
'''
