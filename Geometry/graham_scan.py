import functools
from functools import cmp_to_key

def ccw(p1, p2, p3):
    val = ((p2[0] - p1[0]) * (p3[1] - p1[1]) -
           (p2[1] - p1[1]) * (p3[0] - p1[0]))
    if val > 0:  # 반시계
        return 1
    elif val < 0:  # 시계
        return -1
    else:  # 직선
        return 0

def sort_counter_clock(points):
    pivot = min(points, key=lambda p: (p[1], p[0]))

    def compare(p1, p2):
        order = ccw(pivot, p1, p2)

        if order == 0:
            dist1 = (pivot[0] - p1[0]) ** 2 + (pivot[1] - p1[1]) ** 2
            dist2 = (pivot[0] - p2[0]) ** 2 + (pivot[1] - p2[1]) ** 2
            return -1 if dist1 < dist2 else 1
        return -order
    sorted_points = sorted([p for p in points if p != pivot], key=functools.cmp_to_key(compare))

    return [pivot] + sorted_points

def graham_scan(ordered_points):
    stack = []

    for point in ordered_points:
        while len(stack) >= 2 and ccw(stack[-2], stack[-1], point) <= 0:
            stack.pop()

        stack.append(point)

    return stack

ls = []
ans = 0

n = input()

for _ in range(int(n)):
    a, b = map(int, input().split(" "))
    ls.append((a, b))

ls = sort_counter_clock(ls)
ls = graham_scan(ls)

ls.sort()

print(ls)

n = len(ls)

print(n)

for i in range(n - 3, -1, -1):
    ans += abs((ls[i][0] * ls[i + 1][1] + ls[i + 1][0] * ls[i + 2][1] + ls[i + 2][0] * ls[i][1] -
            (ls[i][1] * ls[i + 1][0] + ls[i + 1][1] * ls[i + 2][0] + ls[i + 2][1] * ls[i][0])))
    print(ans)

print(f'{ans * 1 / 2:.1f}')
