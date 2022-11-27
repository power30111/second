#https://www.acmicpc.net/problem/7576
import sys
from collections import deque
input= sys.stdin.readline

M,N=map(int,input().split())
array=[[]for i in range(N)]
dis_x=[0,0,-1,1]
dis_y=[1,-1,0,0]
def BFS():
    global count
    stack=deque()
    for i,j in tomato:
        stack.append([i,j])
    if not stack:
        return
    count_x,count_y=stack.pop()
    stack.append([count_x,count_y])
    while stack:
        x,y=stack.popleft()
        for i in range(4):
            now_x=x+dis_x[i]
            now_y=y+dis_y[i]
            if now_x<0 or now_y<0 or now_x>=N or now_y>=M:
                continue
            if array[now_x][now_y]=='0':
                stack.append([now_x,now_y])
                array[now_x][now_y]=1

        if count_x==x and count_y==y:
            if stack:
                count_x,count_y=stack.pop()
                stack.append([count_x,count_y])
                count+=1        
tomato=[] 
count=0
for i in range(N):
    array[i]=list(input().split())
for i in range(N):
    for j in range(M):
        if array[i][j]=='1':
            tomato.append([i,j])
BFS()
for i in range(N):
    if '0' in array[i]:
        print("-1")
        exit()
print(count)
#대충 BFS는 알겟는데 시간이 지났다는 것을 언제 체크할지에 대해서 문제가 있었다.
#맨 마지막 stack부분이 pop될때마다 시간이 지난것으로 체크해서 해결했다.
