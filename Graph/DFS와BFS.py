#https://www.acmicpc.net/problem/1260
import sys
from collections import deque
input = sys.stdin.readline

N,M,V = map(int,input().split())
DFS_array,BFS_array=[],[]
array= [[] for i in range(N+M)]
visit=[False]*(N+1)
for i in range(1,M+1):
    A,B = map(int,input().split())
    array[A].append(B)
    array[B].append(A)
for i in range(1,M+1):
    array[i].sort()
def DFS(array,V,visit):
    visit[V]=True
    print(V, end=" ")
    for i in array[V]:
        if not visit[i]:
            DFS(array,i,visit)
            
def BFS(array,V,visit):
    Q = deque([V])
    visit[V]=True
    while Q:
        V = Q.popleft()
        print(V,end=" ")
        for i in array[V]:
            if not visit[i]:
                Q.append(i)
                visit[i]=True
DFS(array,V,visit)
print()
visit=[False]*(N+1)
BFS(array,V,visit)
