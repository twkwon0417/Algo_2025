N = int(input())

ls = [[0] * 3]
for _ in range(N):
    ls.append(list(map(int, input().split(" "))))

dp = [[0] * 3 for _ in range(N + 1)]  # dp[n번째][끝나는]  0 = R, 1 = G, 2 = B

# 시작이 R
dp[1][0] = ls[1][0]
dp[1][1] = float('inf')
dp[1][2] = float('inf')
for i in range(2, N  + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + ls[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + ls[i][1]
    dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + ls[i][2]

r_min = min(dp[N][1], dp[N][2])


# 시작이 G
dp[1][0] = float('inf')
dp[1][1] = ls[1][1]
dp[1][2] = float('inf')
for i in range(2, N  + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + ls[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + ls[i][1]
    dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + ls[i][2]

g_min = min(dp[N][0], dp[N][2])

# 시작이 B
dp[1][0] = float('inf')
dp[1][1] = float('inf')
dp[1][2] = ls[1][2]
for i in range(2, N  + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + ls[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + ls[i][1]
    dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + ls[i][2]

b_min = min(dp[N][0], dp[N][1])

print(min(r_min, g_min, b_min))