#        가위,바위,보가 이기는 경우
win = [0, 3, 1, 2]
cheolsu, younghui = map(int, input().split())
if win[cheolsu] == younghui: print("철수 승")
elif win[younghui] == cheolsu: print("영희 승")
elif cheolsu == younghui:print("비김")