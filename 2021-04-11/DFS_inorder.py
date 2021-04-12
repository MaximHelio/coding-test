def DFS(v):
    if v > 7: return
    else:
        DFS(v*2)
        print(v)
        DFS(v*2+1)

if __name__ == "__main__":
    DFS(1)