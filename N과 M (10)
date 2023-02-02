#https://www.acmicpc.net/problem/15664
import sys
from collections import deque,Counter
from itertools import combinations
input = sys.stdin.readline

N,M=map(int,input().split())
#N개의 수들중에 M의 길이를 만족하는 오름차순인 수열
array=sorted(list(map(int,input().split())))
result=set()
for i in combinations(array,M):
    result.add(i)
result=sorted(list(result))
for i in result:
    for j in i:
        print(j,end=" ")
    print()
