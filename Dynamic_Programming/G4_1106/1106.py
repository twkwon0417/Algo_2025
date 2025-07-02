a, b = map(int, input().split(" "))

ls= []
dp = [100004] * 100204


for _ in range(b):
    tmp1, tmp2 = map(int, input().split(" "))
    ls.append((tmp1, tmp2))
    dp[tmp2] = min(tmp1, dp[tmp2])

for i in range(100004):
    for tup in ls:
        dp[i + tup[1]] = min(dp[i + tup[1]], dp[i] + tup[0])

ans = 100004
for i in range(a, len(dp)):
    ans = min(ans, dp[i])
print(ans)