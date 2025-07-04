N, S = map(int, input().split(" "))

temp = list(map(int, input().split(" ")))
ls = [0] +  temp + [float('inf')]

head, tail = 0, 0
ans = 1e9

tmp = 0
while head <= N:
    if tmp >= S:
        tmp = tmp - ls[tail]
        ans = min((head - tail + 1), ans)
        tail += 1
    elif tmp < S:
        head += 1
        tmp += ls[head]

if ans == 1e9:
    print(0)
else:
    print(ans)