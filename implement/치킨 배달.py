#https://www.acmicpc.net/problem/15686
import sys
from collections import deque
from itertools import combinations
input=sys.stdin.readline
N,M=map(int,input().split())
array=[[]for i in range(N)]
result=50000
house=[]
food=[]
#0 빈칸 1은 집 2는 치킨집
#N=도시 크기  M=유지시킬 치킨집
#거리 공식= |r1-r2|+|c1-c2|
for i in range(N):
    array[i]=list(map(int,input().split()))
    for j in range(len(array[i])):
        if array[i][j]==1:
            house.append([i,j])
        if array[i][j]==2:
            food.append([i,j])
for i in combinations(food,M):  #치킨집의 경우의 수
    min_road=0
    for j,k in house:           #집의 x(j),y(k) 좌표
        road=50000
        for A,B in i:           #경우의수 에 있는 치킨집의 좌표x(A),y(B) 
            road=min(road,abs(j-A)+abs(k-B))       #집의 좌표와 가능한 치킨집들 중에 가장짧은걸로 길이측정.
        min_road+=road
    result=min(min_road,result)
print(result)