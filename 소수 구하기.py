#https://www.acmicpc.net/problem/1929

import sys
from collections import deque
input = sys.stdin.readline

M,N =map(int,input().split())
array=[True]*(N+1)
array[1]=False
for i in range(2,int(N**0.5)+1):
    j = i*i
    while j<N+1 :
        array[j]=False
        j+=i
for i in range(M,N+1):
    if array[i]==True:
        print(i)
    