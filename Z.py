#https://www.acmicpc.net/problem/1074
import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
array = deque()
N,r,c = map(int,input().split())
count=0
def check(N,x,y):
    global count
    if x == r and y== c:
        print(count)
        exit()
    if N==1:
        count+=1
        return
    if not(x <= r <x+N and y<= c < y+N):
        count+=N*N
        return
    dis = N//2
    check(dis,x,y)        
    check(dis,x,y+dis)
    check(dis,x+dis,y)
    check(dis,x+dis,y+dis)
    
check(2**N,0,0)
print(count)