#https://www.acmicpc.net/problem/1389
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
array=[[] for i in range(N+M)]
visit=[False]*(N+M)
for i in range(M):
    A,B = map(int,input().split())
    array[A].append(B)
    array[B].append(A)
for i in range(1,M+1):
    array[i].sort()
def BFS(array,V):
    Q = deque([V])
    num=[0]*(N+1)
    visit[V]=True
    while Q:
        V = Q.popleft()
        for i in array[V]:
            if not visit[i]:
                Q.append(i)
                visit[i]=True
                num[i]=num[V]+1
    return sum(num)
B=1000000
result=[]
for i in range(1,N+1):
    result.append(BFS(array,i))
    visit = [False] * (N + 1)
print(result.index(min(result))+1)
