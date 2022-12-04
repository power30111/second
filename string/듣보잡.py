#https://www.acmicpc.net/problem/1764
import sys
from collections import deque
input=sys.stdin.readline

N,M=map(int,input().split())
N_array=[]
M_array={}
result=[]
for i in range(N):
    N_array.append(input().rstrip())
for i in range(M):
    A=input().rstrip()
    M_array[A]=True
for i in N_array:
    if M_array.get(i):
        result.append(i)
result.sort()
print(len(result))
for i in result:
    print(i)
