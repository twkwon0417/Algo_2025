a = input()

n, m = 504, 504
ls = []

dp = [[0] * m for _ in range(n)]
result = [0] * n

for _ in range(int(a)):
    ls.append(list(map(int, input().split())))

# for i in ls:
#     print(i)

dp[1][1] = ls[0][0]

for i in range(1, int(a) + 1):
    for j in range(1, i + 1):
        dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + ls[i - 1][j - 1]

print(max(dp[int(a)]))
