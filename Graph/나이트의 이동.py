#https://www.acmicpc.net/problem/7562
import sys
from collections import deque
input=sys.stdin.readline
T=int(input())
dis_x=[-2,-1,1,2,-2,-1,2,1] #나이트가 이동할수 있는 경우의 수
dis_y=[1,2,2,1,-1,-2,-1,-2]
def BFS():
    stack=deque()
    stack.append([knight_x,knight_y])
    array[knight_x][knight_y]=1
    while stack:
        x,y=stack.popleft()
        for i in range(8):
            now_x=x+dis_x[i]
            now_y=y+dis_y[i]
            if now_x<0 or now_y<0 or now_x>=N or now_y>=N:
                continue
            if array[now_x][now_y]!=0:
                continue
            stack.append([now_x,now_y])
            array[now_x][now_y]=array[x][y]+1
            if now_x==target_x and now_y==target_y:
                return


for i in range(T):
    count=0
    N=int(input())
    array=[[0 for i in range(N)]for j in range(N)]
    knight_x,knight_y=map(int,input().split())
    target_x,target_y=map(int,input().split())
    BFS()
    print(array[target_x][target_y]-1)