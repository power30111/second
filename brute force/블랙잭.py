#https://www.acmicpc.net/problem/2798
import sys
from collections import deque
from itertools import permutations
input=sys.stdin.readline

N,M=map(int,input().split())
array=list(map(int,input().split()))
now_max=0
for i in permutations(array,3):
    now=0
    
    for j in range(3):
        now+=i[j]
    if M-now>=0 and now_max<now:
        now_max=now
print(now_max)