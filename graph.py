from functools import cmp_to_key
def compare(item1, item2):
    if item1[0] < item2[0]:
        return -1
    elif item1[0] > item2[0]:
        return 1
    else:
        return 0
class DSU:
    def __init__(self, x):
        self.parent = [i for i in range(x)]
        self.rank = [1 for i in range(x)]
    
    def find(self,x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[self.parent[x]])
        return self.parent[x]

    def union(self,u,v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u != parent_v:
            rank_u = self.rank[parent_u]
            rank_v = self.rank[parent_v]
            if rank_u < rank_v:
                self.parent[parent_u] = parent_v
            elif rank_u > rank_v:
                self.parent[parent_v] = parent_u
            else:
                self.parent[parent_v] = parent_u
                self.rank[parent_u] += 1
            return True
        return False

A = 3
B = [
  [1, 2, 1],
  [2, 3, 1],
  [3, 1, 1]
]

edges = []
map = {}
for i in range(len(B)):
    edges.append([B[i][2], i])
    map[(B[i][0],B[i][1])] = i
edges = sorted(edges, key=cmp_to_key(compare))
dsu = DSU(A+1)
ans = [0 for i in range(len(edges))]
for i in range(len(edges)):
    u = B[edges[i][1]][0]
    v = B[edges[i][1]][1]
    flag = dsu.union(u,v)
    if flag:
        ans[map[u,v]] = 1
print(ans)

 