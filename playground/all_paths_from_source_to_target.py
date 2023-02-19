class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        routes = []

        def dfs(route, node):
            nonlocal routes
            if not graph[node]:
                return
            if node == len(graph)-1:
                routes.append(list(route))
                return
            for path in graph[node]:
                route.append(path)
                dfs(route, path)
                route.pop()

        dfs([], 0)

        return routes


g1 = [[1, 2], [3], [3], []]
sol = Solution()
print(sol.allPathsSourceTarget(g1))
