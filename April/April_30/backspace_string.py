class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sI = len(s)-1
        tI = len(t)-1
        
        def backspace(a, I):
            B = 0
            while I >= 0:
                if a[I] == "#":
                    B += 1
                elif B > 0:
                    B -= 1
                else:
                    break
                I -= 1
            
            return I
        
        while sI >= 0 and tI >= 0:
            sI = backspace(s, sI)
            tI = backspace(t, tI)
            
            if sI < 0 or tI < 0:
                break
            
            if s[sI] != t[tI]:
                return False
            
            sI -= 1
            tI -= 1
        
        sI = backspace(s, sI)
        tI = backspace(t, tI)
        
        if sI != tI:
            return False
        
        return True
