# 전위 순회 방식
def DFS(v):
    if v > 7: # 경계값
        return
    else:
        print(v)
        DFS(v*2)
        DFS(v*2+1)

# if __name__ == "__main__":
DFS(1)