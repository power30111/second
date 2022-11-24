#https://www.acmicpc.net/problem/1012
import sys
from collections import deque
sys.setrecursionlimit(100000)
input = sys.stdin.readline
#DFS,BFS에 대해서 알고 푼코드

T=int(input())  #M=가로 N=세로
dis_x=[0,0,1,-1]
dis_y=[1,-1,0,0]
def DFS(now_x,now_y):
    array[now_x][now_y]=0
    for i in range(4):
        if now_x+dis_x[i]>=N or now_y+dis_y[i]>=M or now_x+dis_x[i]<0 or now_y+dis_y[i]<0:
            continue
        if array[now_x+dis_x[i]][now_y+dis_y[i]]==1:
            array[now_x+dis_x[i]][now_y+dis_y[i]]=0
            DFS(now_x+dis_x[i],now_y+dis_y[i])
    return 1
    
        
for A in range(T):
    count=0
    M,N,K=map(int,input().split())
    array=[[0 for i in range(M)]for j in range(N)]
    for i in range(K):
        X,Y=map(int,input().split())
        array[Y][X]=1
    for i in range(N):
        for j in range(M):
            if array[i][j]==1:
                result=DFS(i,j)
                count+=result
    print(count)
                
