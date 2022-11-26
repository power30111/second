import sys
from collections import deque,Counter
input = sys.stdin.readline

N,M,V = map(int,input().split())
array=[[] for i in range(N+M)]
visit=[True]+[False]*(N)
for i in range(M):
    A,B=map(int,input().split())
    array[A].append(B)
    array[B].append(A)
for i in range(1,M+1):
    array[i].sort()
def DFS(array,visit,V):
    visit[V]=True
    print(V,end=" ")
    for i in array[V]:
        if not visit[i]:
            DFS(array,visit,i)
            
def BFS(array,visit,V):
    queue = deque([V])
    visit[V]=True
    while queue:
        x=queue.popleft()
        print(x,end=" ")
        for i in array[x]:
            if not visit[i]:
                queue.append(i)
                visit[i]=True
DFS(array,visit,V)
visit=[False]*(N+1)
print()
BFS(array,visit,V)