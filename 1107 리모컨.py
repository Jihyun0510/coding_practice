# n = 5457
n= int(input())

m = int(input())

# malfuncs = [6,7,8]
malfuncs = map(int, input().split())
now = 100

# +,- 사용할 시
answer = abs(n - now)

# 채널 버튼을 누르고 +,-을 사용할 시
for channel in range(100000):
    # 버튼으로 누를 수 있는 숫자인지 체크
    for num in list(str(channel)):
        if int(num) in malfuncs:
            break
    # 다 누를 수 있다면, 해당 숫자에서 +,-을 사용할 시
    else:
        # if abs(n-channel)+1 < answer:
        #     print(channel)
        answer = min(answer, abs(n-channel)+len(str(channel)))
        

print(answer)

