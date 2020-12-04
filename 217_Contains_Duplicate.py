#217. Contains Duplicate

def containsDuplicate(nums):
    flag = False
    leng_nums = len(nums)
#   for i in range(0,leng_nums):
#       j = i + 1
#       while j < leng_nums:
#           if nums[i] != nums[j]:
#               j += 1
#           else:
#               flag = True
#               break
#   return flag
    
    # hash table
#     hash_map = {}
#     for i in range(len(nums)):
#         if nums[i] not in hash_map.keys():
#             hash_map[nums[i]] = i
#         else:
#             return True
#     return False

    # sorted list
    nums.sort()
    for i in range(1,leng_nums):
        if(nums[i]==nums[i-1]):
            flag = True
    return flag
    
l = [1]
r = containsDuplicate(l)
print(r)