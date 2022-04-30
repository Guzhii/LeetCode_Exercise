class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = {}
        edge = {}
        for l in equations:
            i = equations.index(l)
            x = l[0]
            y = l[1]
            if x not in adj:
                adj[x] = set()
            if y not in adj:
                adj[y] = set()
            adj[x].add(y)
            adj[y].add(x)
            edge[(x,y)] = values[i]
            edge[(y,x)] = 1 / values[i]
            
        def dfs(src, dest, result):
            if src == dest: 
                return result
            if src in self.visited:
                return -1
            
            self.visited.add(src)
            adj_tmp = adj[src]
            
            for a in adj_tmp:
                if a not in self.visited:
                    result = result*edge[(src,a)]
                    tmp = dfs(a, dest, result)
                    if tmp != -1:
                        return tmp
                    result = result/edge[(src,a)]
            return 
                              
        res = []
        result = -1.0
        for i,j in queries:
            result = -1.0
            self.visited = set()
            if i not in adj or j not in adj:
                pass
            else:
                result = dfs(i,j,1.0)
            res.append(result)
        return res
