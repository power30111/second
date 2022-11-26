#https://www.acmicpc.net/problem/7576
import sys
from collections import deque
input= sys.stdin.readline

M,N=map(int,input().split())
array=[[]for i in range(N)]

for i in range(N):
    array[i]=list(input().split())

