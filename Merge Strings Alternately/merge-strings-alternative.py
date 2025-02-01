class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        a = []
        Min = min(len(word1), len(word2))
        for i in range(Min):
                a.append(word1[i])
                a.append(word2[i])
        a.append(word1[Min:] + word2[Min:])
        Str = ''.join(a)
        return(Str)
                

a = Solution()
print(a.mergeAlternately("" , "eddine"))

