class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        n_0 = [s.count("0") for s in strs]
        n_1 = [s.count("1") for s in strs]
        
        @lru_cache(None)
        def dp(md, nd, k):
            if (md < 0) or (nd < 0):
                return float('-inf')
            if k == len(strs):
                return 0
            tmp_0 = n_0[k]
            tmp_1 = n_1[k]
            return max(1+dp(md-tmp_0, nd-tmp_1, k+1), dp(md, nd, k+1))
        
        return dp(m, n, 0)
