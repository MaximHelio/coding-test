def order(node):
    if node <= N:
        if type(tree[node]) is str:
            left_value = order(left[node])
            right_value = order(right[node])
            if tree[node] == '+':
                tree[node] = left_value + right_value
            elif tree[node] == '-':
                tree[node] = left_value - right_value
            elif tree[node] == '*':
                tree[node] = left_value * right_value
            elif tree[node] == '/':
                tree[node] = left_value / right_value
        return tree[node]

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    lst = ['+', '-', '*', '/']
    for _ in range(N):
        idx, value, *arg = map(str, input().split())
        idx = int(idx)
        if value not in lst:
            value = int(value)
        tree[idx] = value
        if arg:
            left[idx] = int(arg[0])
            if len(arg) == 2:
                right[idx] = int(arg[1])
    result = order(1)
    print('#%d %d' %(tc, int(result)))
