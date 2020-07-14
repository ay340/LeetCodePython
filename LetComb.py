#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dct = {"2": ['a', 'b', 'c'],
              "3": ['d','e','f'],
              "4": ['g','h','i'],
              "5": ['j','k','l'],
              "6": ['m','n','o'],
              "7": ['p','q','r','s'],
              "8": ['t','u','v'],
              "9": ['w','x','y','z']}
        
        def addLetter(ch, l):
            if l == []:
                l = [""]
            newL = []
            for el in l:
                for let in dct[ch]:
                    newL.append(el + let)
            return newL
        
        l = []
        for ch in digits:
            l = addLetter(ch,l)
    
        return l
