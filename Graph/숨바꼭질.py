#https://www.acmicpc.net/problem/1697
import sys
from collections import deque
input = sys.stdin.readline

N,X=map(int,input().split())
array=[0 for i in range(150000)]
dis=[-1,+1]
def BFS():
    stack=deque()
    stack.append(N)
    array[N]=1
    while stack:
        now_number=stack.popleft()  #현재 숫자.
        if now_number<0:
                continue
        if now_number*2<len(array):
            if array[now_number*2]==0:
                stack.append(now_number*2)
                array[now_number*2]=array[now_number]+1
        for i in range(2):
            if now_number<0:
                continue
            if now_number+dis[i]<len(array):
                if array[now_number+dis[i]]==0:
                    stack.append(now_number+dis[i])
                    array[now_number+dis[i]]=array[now_number]+1
BFS()
print(array[X]-1)
