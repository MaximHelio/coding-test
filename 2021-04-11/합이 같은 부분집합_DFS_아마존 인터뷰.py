# N개의 원소로 구성된 자연수 집합이 주어지면, 이 집합을 두 개의 부분집합으로 나누었을 때
# 두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 "YES"를 출력하고,
# 그렇지 않으면 "NO"를 출력하는 프로그램을 작성하세요.
# 예를 들어 {1, 3, 5, 6, 7, 10}이 입력되면 {1, 3, 5, 7} = {6, 10}으로
# 두 부분 집합의 합이 15으로 같은 경우가 존재하는 것을 알 수 있다.
# 첫 번째 줄에 자연수 N이 주어진다.
# 입력: 두 번째 줄에 집합의 원소 N개가 주어진다. 각 원소는 중복되지 않는다.
# 출력: 첫번째 줄에 "YES"또는 "NO"를 출력한다.
import sys

def DFS(L, sum):
    if sum > total//2:
        return
    if L == N: # 0번 인덱스부터 사용했으므로
        if sum == (total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum + a[L])
        DFS(L+1, sum)


if __name__ == "__main__":
    N= int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")