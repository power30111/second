#https://www.acmicpc.net/problem/2178
import sys
from collections import deque
input = sys.stdin.readline
miro=[]
N,M = map(int,input().split())
dis_x=[0,0,1,-1]
dis_y=[1,-1,0,0]
for i in range(N):
    miro.append(list(map(int,input().rstrip())))
def BFS():
    stack=deque()
    stack.append([0,0])
    while stack:
        X,Y=map(int,stack.popleft())
        for i in range(4):
            if X+dis_x[i]<0 or Y+dis_y[i]<0 or X+dis_x[i]>=N or Y+dis_y[i]>=M:
                continue
            if miro[X+dis_x[i]][Y+dis_y[i]]==0:
                continue
            if miro[X+dis_x[i]][Y+dis_y[i]]==1:
                stack.append([X+dis_x[i],Y+dis_y[i]])
                miro[X+dis_x[i]][Y+dis_y[i]]=miro[X][Y]+1
BFS()
print(miro[N-1][M-1])
