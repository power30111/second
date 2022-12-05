#https://www.acmicpc.net/problem/11399
import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
array=list(map(int,input().split()))
array.sort()
array2=[]
result=0
for i in array:
    array2.append(i)
    result+=sum(array2)

print(result)