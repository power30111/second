#https://www.acmicpc.net/problem/16236
from collections import deque
import sys, copy
input=sys.stdin.readline

#아기상어 초기크기 = 2 자기보다 큰물고기위치는 못감, 자기랑 같은 크기면 못먹지만 갈순있음
#자기 크기만큼 물고기를 먹으면 크기가 1만큼 커진다. 물고기를 먹게되면 그자리는 빈칸이된다.

N=int(input())
array=[[] for i in range(N)]
size,time=2,0
dis_x=[-1,0,0,1]
dis_y=[0,-1,1,0]
#0=빈칸 1,2,3,4,5,6= 물고기 크기 9=아기상어위치
for i in range(N):
    array[i]=input().split()
    for j in range(N):
        if array[i][j]=='9':
            baby_shark=[i,j]
            array[i][j]='0'

def BFS(size,time,baby_shark):
    fishbowl=copy.deepcopy(array)
    Queue=deque()
    Queue.append([baby_shark[0],baby_shark[1]])
    eat_count=0
    while Queue:
        x,y=Queue.popleft()
        if size==3:
            print("hi")
        if eat_count == size:
            size+=1
            eat_count=0
        for i in range(4):
            now_x=int(x)+dis_x[i]
            now_y=int(y)+dis_y[i]
            
            if now_x < 0 or now_y < 0 or now_x>=N or now_y>=N:  #어항을 벗어나지않아
                continue
            if int(fishbowl[now_x][now_y])>size:                     #내 크기보다 큰곳은 안갈꺼야
                continue
            if int(fishbowl[now_x][now_y])<size and int(fishbowl[now_x][now_y])!= 0:                     #나보다 작은 곳 발견하면 먹을꺼임.
                eat_count+=1
                time+=abs(int(baby_shark[0])-now_x)+abs(int(baby_shark[1])-now_y)
                array[now_x][now_y]='9'
                array[baby_shark[0]][baby_shark[1]]='0'
                fishbowl=copy.deepcopy(array)
                baby_shark=[now_x,now_y]
                Queue=deque()
                Queue.append([baby_shark[0],baby_shark[1]])
                break
            Queue.append([now_x,now_y])
            fishbowl[now_x][now_y]='100'
    return time

print(BFS(size,time,baby_shark))

            
