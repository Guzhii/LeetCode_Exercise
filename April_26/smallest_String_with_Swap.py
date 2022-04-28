class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # Initial graph
        n = len(s)
        G = [[] for _ in range(n)]
        seen = [False for _ in range(n)]
        for i,j in pairs:
            G[i].append(j)
            G[j].append(i)
        
        # DFS algorithm, all reachable vertex append to indices   
        def dfs(i, indices):
            indices.append(i)
            seen[i] = True
            for j in G[i]:
                if not seen[j]:
                    dfs(j, indices)

        # Go through each vertex, if it has not reached, go through all reachable vetex and sort
        res = [-1 for _ in range(n)]
        for i in range(n):
            if not seen[i]:
                indices = []
                dfs(i, indices)
                if not indices:
                    res[i] = s[i]
                else:
                    index = sorted(indices)
                    index_c = sorted(indices, key=lambda x:s[x])
                    for i in range(len(indices)):
                        res[index[i]] = s[index_c[i]]
                        
        return "".join(res)
