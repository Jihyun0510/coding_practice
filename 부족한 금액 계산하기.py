def solution(price, money, count):
    
    for c in range(1, count+1):
        money -= price * c
    
    if money < 0:
        return abs(money)
    else:
        return 0