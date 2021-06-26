from typing import List
from collections import deque


class Solution:
    
        

    def letterCombosHelper(number, n, table):
        # answer array
        result = []
        q = deque()
        q.append("")

        while len(q) != 0:
            s = q.pop()

            # if complete word is generated
            # push it in the list
            if len(s) == n:
                list.append(n)
            else:
                # Try all possible letters for current digit
                # in number[]
                for letter in table

    def letterCombinations(self, digits: str) -> List[str]:
        # table[i] stores all chars that corresponds
        # ith digit in phone
        table = [
            '0', 
            '1', 
            'abc', 
            'def', 
            'ghi', 
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxys'
        ]

        n = len(digits)
        test_list = letterCombinations(digits, n, table)

        s = ""
        for word in test_list:
            s += word + " "

        print(s)
        return 

    




