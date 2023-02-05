#https://www.acmicpc.net/problem/15270
import sys
from collections import deque
input =sys.stdin.readline

N,M=map(int,input().split())
array=[[] for i in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    array[a].append(b)
    array[b].append(a)
#친한 친구들로만 짝지어서 하고싶어. 무대에 최대한 많은 친구들을 세우고싶어= 최대한 많은 짝을 찾기. a->b b->c 라고 a->c 는 아님.
visit=[False]*(N+1)
def DFS(visit,V,cnt):
    visit[V]=True
    cnt+=1
    for i in array[V]:
        if not visit[i]:
            visit[i]=True
            return True
    return False
max_cnt=0

for i in range(1,N+1):
    cnt=0
    if not visit[i]:
        if DFS(visit,i,cnt):
            max_cnt+=2
        else:
            visit[i]=False
if len(visit)-1>max_cnt:
    print(max_cnt+1)
else:
    print(max_cnt)