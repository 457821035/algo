'''
 Created by Gavia on 2018/4/15.
'''

class Solution:
    '''
    Input:
        widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
        S = "bbbcccdddaaa"
    Output: [2, 4]
    Explanation:
        All letters except 'a' have the same length of 10, and
        "bbbcccdddaa" will cover 9 * 10 + 2 * 4 = 98 units.
        For the last 'a', it is written on the second line because
        there is only 2 units left in the first line.
        So the answer is 2 lines, plus 4 units in the second line.
    '''
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        if len(S) == 0:
            return 0, 0

        lines, thisLine = 1, 0

        for c in S:
            thisLine = widths[ord(c) - ord('a')] + thisLine
            print('thisLine', thisLine)
            if thisLine > 100:
               lines += 1
               thisLine = widths[ord(c) - ord('a')]
        return lines, thisLine


solution = Solution()
print(solution.numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],'abcdefghijklmnopqrstuvwxyz'))
