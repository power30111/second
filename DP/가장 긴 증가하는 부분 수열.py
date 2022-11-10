#https://www.acmicpc.net/problem/11053
import sys
from collections import deque,Counter
input = sys.stdin.readline

A=int(input())
array=list(map(int,input().split()))
result=[1 for i in range(A)]

for i in range(A):
    for j in range(i):
        print(result,j)
        if array[i]>array[j]:
            result[i]=max(result[i],result[j]+1)
print(max(result))