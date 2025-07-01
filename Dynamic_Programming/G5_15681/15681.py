import sys
from collections import defaultdict

sys.setrecursionlimit(100000)

a, b, c = map(int, input().split(" "))

ls = defaultdict(list)
dp = [1] * (a + 1)
visited = [False] * (a + 1)

def dfs(val):
    visited[val] = True
    for i in ls[val]:
        if visited[i] == False:
            dfs(i)
            dp[val] += dp[i]

    return None

for _ in range(a - 1):
    tmp1, tmp2 = map(int, input().split(" "))
    ls[tmp1].append(tmp2)
    ls[tmp2].append(tmp1)

dfs(b)

for i in range(c):
    temp = int(input())
    print(dp[temp])
