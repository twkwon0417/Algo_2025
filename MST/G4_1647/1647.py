import heapq
from collections import defaultdict

ans = []
N, M = map(int, input().split(" "))

ls = defaultdict(list)

for _ in range(M):
    a, b, c = map(int, input().split(" "))
    ls[a].append((c, b))
    ls[b].append((c, a))

visited = [False] * (N + 1)
adj = []

visited[1] = True
for tup in ls[1]:
    heapq.heappush(adj, tup)

for _ in range(N - 1):
    tmp = int
    while True:
        tmp = heapq.heappop(adj)
        if visited[tmp[1]] == False:
            visited[tmp[1]] = True
            break

    ans.append(tmp[0])
    for tup in ls[tmp[1]]:
        heapq.heappush(adj, tup)

print(sum(ans) - max(ans))