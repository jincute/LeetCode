class Solution(object):
    """
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """
    '''
    样例 1:
	输入:   {
		"dog",
		"google",
		"facebook",
		"internationalization",
		"blabla"
		}
	输出: ["internationalization"]



样例 2:
	输入: {
		"like",
		"love",
		"hate",
		"yes"
		}
	输出: ["like", "love", "hate"]
    '''

    # Accepted, 915ms
    def longestWords(self, dictionary):
        # write your code here
        max_len = 0
        longdic = []
        for word in dictionary:
            wordlen = len(word)
            if wordlen == max_len:
                longdic.append(word)
            elif wordlen > max_len:
                longdic = []
                longdic.append(word)
                max_len = wordlen
        return longdic

S = Solution()
a = S.longestWords(["like", "love", "hate", "yes"])
print(a)
