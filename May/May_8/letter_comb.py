class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        
        res = [""]
        for d in digits:
            map_str = map[d]
            res = [a + b for a in res for b in map_str]
        
        if res == [""]:
            res = []
        return res
