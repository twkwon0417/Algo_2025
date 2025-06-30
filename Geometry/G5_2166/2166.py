ls = []
ans = 0

n = int(input())

for _ in range(n):
    a, b = map(int, input().split(" "))
    ls.append((a, b))
ls.append(ls[0])

for i in range(n):
    ans += ls[i][0] * ls[i+1][1] - ls[i+1][0] * ls[i][1]

print(abs(ans) / 2)
