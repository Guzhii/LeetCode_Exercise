class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        S = []
        T = []
        sI = 0
        tI = 0
        
        for i in s:
            if i == "#":
                if sI > 0:
                    sI -= 1
            else:
                S.insert(sI, i)
                sI += 1
                
        for j in t:
            if j == "#":
                if tI > 0:
                    tI -= 1
            else:
                T.insert(tI, j)
                tI += 1
        
        return S[:sI] == T[:tI]
