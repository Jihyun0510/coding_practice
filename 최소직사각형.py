def solution(sizes):
    answer = 0
    height = 0
    width = 0
    # 긴변이 height, 짧은 변이 width
    for card in sizes:
        
        if max(card) > height:
            height = max(card)
        if min(card) > width:
            width = min(card)
            
    return height * width