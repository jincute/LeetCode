"""
Ex4:
Input: "([)]"
Output: false
Ex5:
Input: "{[]}"
Output: true
"""
import pdb
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        def getValue(t):
            if t == '(':
                return 1
            elif t == ')':
                return -1
            elif t == '[':
                return 2
            elif t == ']':
                return -2
            elif t == '{':
                return 3
            elif t == '}':
                return -3

        symbol = list(s)
        l = len(symbol)
        j = []
        flag = True
        if s != "":
            for i in range(0,l):
                #print(i)
                if getValue(symbol[i])>0:
                    j.append(symbol[i])
                    #print(j)
                else:
                    #print(j)
                    if j == []:
                        flag = False
                        break
                    else:
                        #print(symbol[i])
                        #print(getValue(symbol[i]))
                        #print(j.pop())
                        #print(abs(getValue(j.pop())))
                        if (abs(getValue(j.pop()))) != abs(getValue(symbol[i])):
                            flag = False
                            break
            if j != []:
                flag = False
        return flag

"""
        n = len(s)
        if n == 0:
            return True

        if n % 2 != 0:
            return False

        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')

        if s == '':
            return True
        else:
            return False


A = Solution()
print(A.isValid("{[]}"))   #True
print(A.isValid("(])"))    #False
print(A.isValid(")"))  #False
print(A.isValid("["))  #False

"""
Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
