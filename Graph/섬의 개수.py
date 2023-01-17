#https://www.acmicpc.net/problem/4963
import sys, copy
from collections import deque
input=sys.stdin.readline

dis_x=[0,0,1,-1,-1,1,-1,1]
dis_y=[1,-1,0,0,-1,1,1,-1]
def BFS(array,a,b):
    Queue=deque()
    Queue.append([a,b])
    while Queue:
        x,y=Queue.popleft()
        for i in range(8):
            now_x=int(dis_x[i]+x)
            now_y=int(dis_y[i]+y)
            if now_x < 0 or now_y < 0 or now_x>=h or now_y>=w:
                continue
            if array[now_x][now_y]=='0':
                continue
            array[now_x][now_y]='0'
            Queue.append([now_x,now_y])
    
            
while True:
    cnt=0
    w,h=map(int,input().split())
    if w==0 and h ==0:
        exit()
    array=[[]for i in range(h)]
    for i in range(h):
        array[i]=input().split()
    #1=땅 0=바다
    for i in range(h):
        for j in range(w):
            if array[i][j]=='1':
                BFS(array,i,j)
                cnt+=1
    print(cnt)
    
    