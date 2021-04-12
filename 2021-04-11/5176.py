def dfs(v):
    global cnt
    if v <= N:
        dfs(v*2)
        tree[v] = cnt
        cnt += 1
        dfs(v*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    cnt = 1
    dfs(1)
    print('#%d %d %d' %(tc, tree[1], tree[N//2]))
