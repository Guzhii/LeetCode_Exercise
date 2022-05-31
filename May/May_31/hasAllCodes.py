class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        got = set()
        
        for i in range(len(s)-k+1):
            cur = s[i:i+k]
            if cur not in got:
                got.add(cur)
                need -= 1
                
                if need == 0:
                    return True
        
        return False
