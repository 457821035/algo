'''
Created by Gavia on 2018/4/25.
'''
class Solution:
    '''
    Given a List of words, return the words that can be
    typed using letters of alphabet on only one row's of American keyboard like the image below.

    Input: ["Hello", "Alaska", "Dad", "Peace"]
    Output: ["Alaska", "Dad"]
    '''
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = [['q','w','e','r','t','y','u','i','o','p'],['a','s','d','f','g','h','j','k','l'],['z','x','c','v','b','n','m']]
        res = []

        for word in words:
            for keys in keyboard:
                flag = 0
                for char in word.lower():
                    if char in keys:
                        flag = flag + 1
                    if flag == len(word):
                        res.append(word)


        return res

solution = Solution()
print(solution.findWords(["Hello","Alaska","Dad","Peace"]))