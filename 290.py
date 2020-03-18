import pdb

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        #print(pattern.split())
        
        words = str.split(' ')
        if len(pattern) != len(words):
            return False  
        
        letterdict, worddict = {}, {}

        for letter, word in zip(pattern, words):
            print('letterdict: ', letterdict)
            print('worddict: ', worddict)

            if letter not in letterdict:
                letterdict[letter] = word
            if word not in worddict:
                worddict[word] = letter 
            if worddict[word] != letter or letterdict[letter] != word:
                return False  
        return True


pattern = "abacd"
#sent = "dog cat cat dog fish"
sent = "dog cat dog fish cat"
print(Solution().wordPattern(pattern, sent))