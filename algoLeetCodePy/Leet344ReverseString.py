'''
 Created by Gavia on 2018/4/15.
'''

class Solution(object):
    def reverseString(self, s):
        """
        Example:
        Given s = "hello", return "olleh".
        基础递归
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        n = len(s)
        return self.reverseString(s[n//2:]) + self.reverseString(s[:n//2])

    def skip(self, s:str):
        wordS = s.split(' ')
        ans = ''
        for i in wordS:
            ans = ans+' '+self.reverseString(i)

        return ans.strip(' ')
solution = Solution()
input = "hello world in tow"
print('input:', input)
print('normal:', solution.reverseString(input))
print('skip:', solution.skip(input))
