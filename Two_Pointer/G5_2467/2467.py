n = int(input())
ls = list(map(int, input().split(" ")))

left_ptr = 0
right_ptr = n - 1

left_ans = 0
right_ans = n - 1

min_val = 3 * 10e9

while left_ptr != right_ptr:
    if ls[left_ptr] + ls[right_ptr] >= 0:
        if abs(ls[left_ptr] + ls[right_ptr]) < min_val:
            left_ans = left_ptr
            right_ans = right_ptr
            min_val = abs(ls[left_ptr] + ls[right_ptr])
        right_ptr -= 1
    elif ls[left_ptr] + ls[right_ptr] < 0:
        if abs(ls[left_ptr] + ls[right_ptr]) < min_val:
            left_ans = left_ptr
            right_ans = right_ptr
            min_val = abs(ls[left_ptr] + ls[right_ptr])
        left_ptr += 1
print(ls[left_ans], ls[right_ans])