def tr(root):
    global cnt
    if root:
        cnt += 1
        tr(tree[root][0])
        tr(tree[root][1])

T = int(input())
E, N = map(int, input().split())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    tree = [[0, 0] for _ in range(E+2)]
    for idx in range(E):
        parent = arr[2*idx]
        child = arr[2*idx+1]
        if tree[parent][0] == 0:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
    cnt = 0
    tr(N)
    print('#%d %d' %(tc, cnt))