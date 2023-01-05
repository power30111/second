#https://www.acmicpc.net/problem/14502
import sys
from collections import deque
from itertools import combinations
input=sys.stdin.readline

#3개의 벽을 세워야만 한다. 바이러스는 상하좌우 빈칸으로 모두퍼져나갈수있다. 0 빈칸 1 벽 2 바이러스
#벽으로 바이러스를 최대한 막아본다음에 안전 영역의 크기의 최대값을 출력해보자!
#N세로 M가로
N,M=map(int,input().split())
array=[[]for i in range(N)]
dis_x=[0,0,1,-1]
dis_y=[1,-1,0,0]
empty,virus=[],[]
result,cnt=0,0
for i in range(N):
    array[i]=list(map(int,input().split()))
    for j in range(M):
        if array[i][j]==0:
            empty.append([i,j])
        elif array[i][j]==2:
            virus.append([i,j])

def BFS(virus,array):
    now_map=array
    global cnt
    Q=deque()
    for i in range(len(virus)):
        Q.append([virus[i][0],virus[i][1]])
    while Q:
        x,y=Q.popleft()
        for i in range(4):
            now_x=x+dis_x[i]
            now_y=y+dis_y[i]
            if now_x<0 or now_y<0 or now_x>=N or now_y>=M:

                continue
            if now_map[now_x][now_y]==1 or now_map[now_x][now_y]==2:
                continue
            else:
                Q.append([now_x,now_y])
                now_map[now_x][now_y]=2
            
    for i in range(N):
        for j in range(M):
            if now_map[i][j]==0:
                cnt+=1
for i in combinations(empty,3):
    cnt=0
    for j in range(3):
        A,B=i[j]
        array[A][B]=1
    BFS(virus,array)
    for j in range(3):
        A,B=i[j]
        array[A][B]=0
    if result<cnt:
        result=cnt
        
        
print(result)

##문제 풀이
from collections import deque
from itertools import combinations, permutations
import sys,copy
input=sys.stdin.readline

N,M=map(int,input().split())

array=[[]for i in range(N)]
virus=deque()
wall,now=[],0
dis_x=[0,0,1,-1]
dis_y=[1,-1,0,0]
for i in range(N):
    array[i]=input().split()
    for j in range(M):
        if array[i][j] == '2':
            virus.append([i,j])
        if array[i][j] == '0':
            wall.append([i,j])

def BFS(wall_list,N,M):  #바이러스 전염경로
    labo=copy.deepcopy(array)
    for i in range(3):
        labo[int(wall_list[i][0])][int(wall_list[i][1])]='1'
    stack=deque(virus)
    cnt=0
    while stack:
        x,y=stack.popleft()
        for i in range(4):
            now_x=x+dis_x[i]
            now_y=y+dis_y[i]
            if now_x<0 or now_y <0 or now_x>=N or now_y>=M:
                continue
            if labo[now_x][now_y]=="1" or labo[now_x][now_y]=="2":
                continue
            labo[now_x][now_y]='2'
            stack.append([now_x,now_y])
    for i in range(N):
        for j in range(M):
            if labo[i][j]=="0":
                cnt+=1
    return cnt
test=[[0,1],[1,0],[3,5]]
for i in combinations(wall,3):
    wall_list=i
    now_cnt=BFS(wall_list,N,M)
    if now<now_cnt:
        now=now_cnt
print(now)

