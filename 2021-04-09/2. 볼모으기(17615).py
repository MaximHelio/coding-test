N = int(input())
arr = list(input())
cnt = 0 # 공의 이동 횟수
# left = arr[:N//2]
# right = arr[N//2:]
# left_R = left.count('R')
# left_B = left.count('B')
# right_R = right.count('R')
# right_B = right.count('B')

# 독립된 R, B의 개수 찾기
for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        cnt += 1

print(cnt//2)


