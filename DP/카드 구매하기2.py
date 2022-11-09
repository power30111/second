#https://www.acmicpc.net/problem/16194
import sys
from collections import deque,Counter
input = sys.stdin.readline

N=int(input())
P=[0]+list(map(int,input().split()))
arr=list(P)
for i in range(1,N+1):
    for j in range(1,i+1):
        arr[i]=min(arr[i],arr[i-j]+P[j])
print(arr[N])