def solution(price, money, count):
    pay = 0
    for i in range(1,count+1):
        pay += i * price
    if money - pay >= 0:
        return 0
    else:
        return pay - money