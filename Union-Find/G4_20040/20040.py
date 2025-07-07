import sys

sys.setrecursionlimit(100000)
Node, N = map(int, input().split(" "))
ls = [0] * Node

for i in range(Node):
    ls[i] = i

def union(x, y):
    x_parent = find(x)
    y_parent = find(y)
    if x_parent == y_parent:
        return False
    if x_parent < y_parent:
        ls[y_parent] = x_parent
    else:
        ls[x_parent] = y_parent
    return True

def find(x):
    if ls[x] != x:
        ls[x] = find(ls[x])
    return ls[x]

flag = True

for ans in range(N):
    x, y = map(int, input().split(" "))
    if union(x, y) == False:
        flag = False
        print(ans + 1)
        break

if flag:
    print(0)