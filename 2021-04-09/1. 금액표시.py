def tag(price):
    lst = []
    lst.append(price % 1000)
    price = price // 1000
    if price < 1000:
        return

price = int(input())
# splitted_price = price.split()
