class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        '''
        # Failed: Time Limit Exceeded
        '''
        hashcode = 0
        for i in key:
            hashcode = (33*hashcode + ord(i))%HASH_SIZE
        return hashcode
        
S = Solution()
a = S.hashCode("abcd",1000)
