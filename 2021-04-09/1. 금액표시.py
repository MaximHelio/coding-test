def tag(price):
    rem = price % 1000
    global lst
    lst.append(rem)
    price = price // 1000
    if price < 1000:
        lst.append(price)
        return lst
    return tag(price)

price = int(input())
lst = []
tag(price)
lst.reverse()
# print(','.join(lst))
ans = str()
for num in lst:
    ans = ans + str(num) + ','
print(ans[:-1])