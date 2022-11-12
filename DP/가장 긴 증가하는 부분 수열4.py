#https://www.acmicpc.net/problem/14002
import sys
from collections import deque,Counter
input = sys.stdin.readline

N = int(input())
arr=list(map(int,input().split()))
result=[1]*N
stack=[]
for i in range(N):
    for j in range(i):
        if arr[i]>arr[j]:
            result[i]=max(result[i],result[j]+1)
A=max(result)
print(A)
for i in range(N-1,-1,-1):
    if result[i]==A:
        stack.append(arr[i])
        A-=1
stack.reverse()
for i in stack:
    print(i,end=" ")
    

