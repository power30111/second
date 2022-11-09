#https://www.acmicpc.net/problem/2193
import sys
from collections import deque,Counter
input = sys.stdin.readline
#pinary number
array=[[0,1],[1,0],[1,1],[2,1]]   #(맨뒤가 0인 갯수, 맨뒤가 1인갯수)
N=int(input())
for i in range(4,N+1):
    array.append([array[i-1][0]+array[i-2][0],array[i-1][1]+array[i-2][1]])
print(sum(array[N-1]))