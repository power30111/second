#https://www.acmicpc.net/problem/1931
import sys
from collections import deque
input=sys.stdin.readline
visit=[False]*100001
N=int(input())
array=[]
cnt=0
for i in range(N):
    A,B=map(int,input().split())
    array.append(A,B)

