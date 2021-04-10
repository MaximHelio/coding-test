def func(n, st, ed):
    if n==1:
        return(st, ed)
    func(n-1, st, 6-st-ed)
        return()
    func(1, st, ed)
    func(n-1, 6-st-ed, ed)

print(func(3, 1, 2))