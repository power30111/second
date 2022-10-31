#https://www.acmicpc.net/problem/1676
import sys
from collections import deque
input = sys.stdin.readline
count = 0
def check(N,x,y):
    if N==1:
        array[x][y] = count
        count+=1
        array[x+1][y] = count
        count+=1
        array[x][y+1] = count
        count+=1
        array[x+1][y+1] = count 
    
N,r,c = map(int,input().split())
array=[[0 for i in range(2**(N))]for j in range(2**(N))]
