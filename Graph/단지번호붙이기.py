#https://www.acmicpc.net/problem/2667
import sys
from collections import deque
input=sys.stdin.readline
dis_x=[0,0,-1,1]
dis_y=[1,-1,0,0]
def BFS(x,y):
    count=1
    stack=deque()
    stack.append([x,y])
    array[x][y]=0
    while stack:
        now_x,now_y=stack.popleft()
        
        for i in range(4):
            A=now_x+dis_x[i]
            B=now_y+dis_y[i]
            if A>=N or B>=N or A<0 or B<0:
                continue
            if array[A][B]==0:
                continue
            stack.append([A,B])
            array[A][B]=0
            count+=1
    return count    
N=int(input())
result=[]
result2=0
array=[[] for i in range(N)]
for i in range(N):
    array[i]=list(map(int,input().rstrip()))
for i in range(N):
    for j in range(N):
        if array[i][j]==1:
            now=BFS(i,j)
            result.append(now)
            result2+=1
print(result2)
result=sorted(result)
for i in result:
    print(i)
