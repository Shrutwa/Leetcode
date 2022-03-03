class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        def dfs(u):
            res.append(u)
            visited.add(u)
            for v in g[u]:
                if v not in visited:
                    dfs(v)
                
        g = collections.defaultdict(list)
        
        for u,v in adjacentPairs:
            g[u].append(v)
            g[v].append(u)
            
        for k, v in g.items():
            if len(v)==1:
                start = k
                break
                
        visited = set()
        res = []
        
        dfs(start)
        return res