import sys;read=sys.stdin.readline
import heapq

result=[]
for T in range(int(read())):
    # 각 step별 동기화 여부를 기록
    visited=[False]*1_000_001
    # 최소힙, 최대힙 생성
    minH,maxH=[],[]
    
    for i in range(int(read())):
        s=read().split()
        # I 명령어 = 최소힙, 최대힙에 동시에 입력
        # 해당 step은 동기화과 되어있는 것으로 표시 (True)
        if s[0]=='I':
            heapq.heappush(minH,(int(s[1]),i))
            heapq.heappush(maxH,(-int(s[1]),i))
            visited[i]=True
        # D 1 명령어 = 최대힙만 업데이트
        elif s[1]=='1':
            # target인 최대값을 삭제하기 전,
            # 이전에 최소힙에서는 삭제되었지만 아직 동기화되지 않은 값들 모조리 삭제
            while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)
            
            # 삭제할 값이 없다면 실행되지 않고 이번 step은 넘어감
            if maxH:
                # 이번 step은 동기화되지 않았음을 기록
                visited[maxH[0][1]]=False
                # 원래 target이 맨 앞에 있으니 삭제
                heapq.heappop(maxH)
        else:
            # target인 최소값을 삭제하기 전,
            # 이전에 최대힙에서는 삭제되었지만 아직 동기화되지 않은 값들 모조리 삭제
            while minH and not visited[minH[0][1]]:heapq.heappop(minH)
            
            # 삭제할 값이 없다면 실행되지 않고 이번 step은 넘어감
            if minH:
                # 이번 step은 동기화되지 않았음을 기록
                visited[minH[0][1]]=False
                # 원래 target이 맨 앞에 있으니 삭제
                heapq.heappop(minH)
    # 아직 동기화되지 않은 잔여 명령어들을 처리
    while minH and not visited[minH[0][1]]:heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)
    result.append(f'{-maxH[0][0]} {minH[0][0]}'if maxH and minH else'EMPTY')
print('\n'.join(result))