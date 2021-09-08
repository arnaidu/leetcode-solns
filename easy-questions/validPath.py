"""
Question 1971. Find if path Exists in Graph from LeetCode.

The general idea is just to use BFS or DFS in order to find the path, making sure to return once BFS or DFS
detects the end vertex. Both algorithms will begin with the start vertex.

Complexity Analysis:
For the algorithm below, the first two statements are constant cost.
Setting up the adjacency list requires a loop over all edges, where all statements
inside the loop are constant cost. Therefore, the loop is O(E). The BFS algorithm is
known to be O(V + E) for time complexity, and O(V) for memory complexity due to visisted list,
but also O(V + E) for adjacency list. .

Therefore, the time complexity if O(V + E) and the space complexity is O(V + E). 
"""

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        # handle some edge cases
        if start == end:
            return True
        if not edges:
            return False
        # make adjacency list
        adjacency_list = dict()
        for edge in edges:
            if edge[0] in adjacency_list:
                adjacency_list[edge[0]].append(edge[1])
            else:
                adjacency_list[edge[0]] = [edge[1]]
            if edge[1] in adjacency_list:
                adjacency_list[edge[1]].append(edge[0])
            else:
                adjacency_list[edge[1]] = [edge[0]]
        
        visisted = [start]
        queue = [start]
        while queue:
            s = queue.pop(0)
            for neighbour in adjacency_list[s]:
                if neighbour == end:
                    return True
                if neighbour not in visisted:
                    visisted.append(neighbour)
                    queue.append(neighbour)
        return False
        
