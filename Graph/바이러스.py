#https://www.acmicpc.net/problem/2606
import sys
from collections import deque
input=sys.stdin.readline
N=int(input())  #컴퓨터의 개수
M=int(input())  #간선의 개수
array=[[] for i in range(N+1)]
visit=[False]*(N+1)
count=0
for i in range(M):
    A,B=map(int,input().split())
    array[A].append(B)
    array[B].append(A)

def DFS(V):
    global count
    visit[V]=True
    for i in array[V]:
        if not visit[i]:
            count+=1
            DFS(i)
DFS(1)
print(count)