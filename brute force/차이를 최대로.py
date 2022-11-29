#https://www.acmicpc.net/problem/10819
import sys
from collections import deque
from itertools import permutations
input=sys.stdin.readline
N=int(input())
array=list(map(int,input().split()))
result2=0
for i in permutations(array,N):
    result=0
    for j in range(1,len(i)):
        result+=abs(i[j-1]-i[j])
    if result2<result:
        result2=result
print(result2)