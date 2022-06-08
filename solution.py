
import collections

def sol(x, y):

    # BFS
    # bfs through coords a knight can go to
    # return if found target
    # else add to visited and add next moves to queue
    
    q = collections.deque()
    q.append((0, 0))
    visited = set()
    count = 0

    while q:
        
        for i in range(len(q)):
            kx, ky = q.popleft()
            
            if (kx, ky) in visited:
                continue
            
            visited.add((kx, ky))
            if kx == x and ky == y:
                return count
                
            for hori, vert in ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)):
                q.append((kx + hori, ky + vert))
        
        count += 1
    
    
    
print(sol(2, 1))
print(sol(5, 5))
print(sol(25, 50))
