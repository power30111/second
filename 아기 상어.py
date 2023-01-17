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

def BFS(size,time):
    global baby_shark
    fishbowl=copy.deepcopy(array)
    Queue=deque()
    Queue.append([baby_shark[0],baby_shark[1]])
    eat_count=0
    can_eat_list=[]
    while Queue:
        x,y=Queue.popleft()
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
            if int(fishbowl[now_x][now_y])<size and int(fishbowl[now_x][now_y])!= 0:
                Queue.append([x,y])
                while Queue:
                    x,y=Queue.popleft()
                    for i in range(4):
                        now_x=int(x)+dis_x[i]
                        now_y=int(y)+dis_y[i]
                    
                        if now_x < 0 or now_y < 0 or now_x>=N or now_y>=N:  #어항을 벗어나지않아
                            continue
                        if int(fishbowl[now_x][now_y])>size:                     #내 크기보다 큰곳은 안갈꺼야
                            continue
                        if int(fishbowl[now_x][now_y])<size and int(fishbowl[now_x][now_y])!= 0:
                            can_eat_list.append([now_x,now_y])
                dx,dy=can_eat_list[0][0],can_eat_list[0][1]
                for i in range(len(can_eat_list)):
                    if int(dx) > int(can_eat_list[i][0]):
                        dx=int(can_eat_list[i][0])
                        dy=int(can_eat_list[i][1])
                    elif int(dx) == int(can_eat_list[i][0]):
                        if int(dy) > int(can_eat_list[i][1]):
                            dy=int(can_eat_list[i][1])
                            dx=int(can_eat_list[i][0])
                eat_count+=1
                time+=abs(int(baby_shark[0])-dx)+abs(int(baby_shark[1])-dy)
                array[dx][dy]='9'
                array[baby_shark[0]][baby_shark[1]]='0'
                fishbowl=copy.deepcopy(array)
                baby_shark=[dx,dy]
                Queue=deque()
                Queue.append([baby_shark[0],baby_shark[1]])
                can_eat_list=[]
                break
            Queue.append([now_x,now_y])
            fishbowl[now_x][now_y]='100'
    return time

print(BFS(size,time))

            
