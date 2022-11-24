#https://www.acmicpc.net/problem/11724
import sys
from collections import deque
sys.setrecursionlimit(100000)
input=sys.stdin.readline
def DFS(x):
    check[x]=True
    for i in array[x]:
        if not check[i]:
            DFS(i)
N,M=map(int,input().split())
array=[[] for i in range(N+1)]  #1부터 사용할꺼라 N+1.
check=[False]*(N+1)
count=0
for i in range(M):
    A,B=map(int,input().split())
    array[A].append(B)
    array[B].append(A)
for i in range(1,N+1):
    if not check[i]:
        DFS(i)
        count+=1
print(count)
