from collections import deque, defaultdict

def find_girth(n, m, edges):

    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    min_cycle_length = float('inf')

    
    for start in range(1, n + 1):
        visited = [-1] * (n + 1)  
        queue = deque([(start, -1, 0)])
        visited[start] = 0

        while queue:
            node, parent, depth = queue.popleft()

            for neighbor in graph[node]:
                
                if visited[neighbor] == -1:
                    visited[neighbor] = depth + 1
                    queue.append((neighbor, node, depth + 1))

                elif neighbor != parent:
                    cycle_length = depth + visited[neighbor] + 1
                    min_cycle_length = min(min_cycle_length, cycle_length)
                    if min_cycle_length == 3:  
                        return 3

    return min_cycle_length if min_cycle_length != float('inf') else -1


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

girth = find_girth(n, m, edges)
print(girth)
