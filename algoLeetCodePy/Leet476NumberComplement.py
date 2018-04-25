'''
 Created by Gavia on 2018/4/15.
'''

class Solution:
    '''
    Input: 1
    Output: 0
    Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

    Input: 5
    Output: 2
    Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
    '''
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        index = 1
        while index <= num:
            index = index << 1
        ans = (index - 1) ^ num
        print('input: ', bin(num),'ans: ', bin(ans))
        return ans

solution = Solution()
print(solution.findComplement(8))