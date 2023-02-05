import sys
input=sys.stdin.readline

N,M=map(int,input().split())
array=[[]for i in range(N+1)]
for i in range(1,N):
    array[i].append(i+1)
for i in range(M):
    x,y=map(int,input().split())
    array[x].append(y)

#중요한 조건 1. size는 모든 지역의 크기가 동일해야한다. 즉 전체 도시수에서 size로 나누어 떨어지지않으면 틀린것.
#           2. a지역에서 b지역으로 이동하는 길이있다면 b지역에서 a지역으로 가는길이 없어야한다.
#           3. 모든 도시에는 자기다음번호 도시로 가는 고속도로가 존재한다.
#           1번 도시부터 size 1로 시작해서 지역번호를 붙여주면서 그래프를 탐색해본다.
#           탐색중 1,2 번 조건을 위반하는 도시가 있다면 size를 키우고 다시 처음부터 순차탐색해본다.
#           조건을 위반하는 도시가 없으면서 모든도시에 지역번호를 붙였다면 출력하고 끝내자.

def DFS(V,visit,size):
    visit[V]=True
    for i in 
            
    
    
for i in range(1,N+1):
    if N%i !=0:
        continue
    visit=[False]*(N+1)
    size = i
    DFS(i,visit,size)
    print(visit)
    
    