import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split()) # 정점, 간선의 수
g = [[0] *(N+1) for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    g[a][b] = c


for i in range(1, N+1):
    for j in range(1, N+1):
        print(g[i][j], end=" ")
    print()
