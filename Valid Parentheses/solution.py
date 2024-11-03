class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ref = {
            '{':'}',
            '[':']',
            '(':')',
        }
        stack = []
        for char in s:
            if char in ref:
                stack.append(char)
            else:
                if stack and ((ref[stack[-1]]) == char):
                    stack.pop()
                else:
                    return  (False)
        return not stack


string ="{}{}"
test = Solution()
print(test.isValid(string))
