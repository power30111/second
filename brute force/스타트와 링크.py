#https://www.acmicpc.net/problem/14889
import sys
from collections import deque
from itertools import combinations,permutations
input=sys.stdin.readline
N=int(input())
team=[i for i in range(N)]
array=[[]for i in range(N)]
result=99999
for i in range(N):
    array[i]=(list(map(int,input().split())))

for team1 in combinations(team,N//2):
    team1_result=0
    team2_result=0
    count=0
    team2=[i for i in range(N)]
    for i in range(N//2):
        team2.remove(team1[i])
    for j in team1:
        for k in team1:
            team1_result+=array[j][k]
    for j in team2:
        for k in team2:
            team2_result+=array[j][k]
    if result>abs(team1_result-team2_result):
        result=abs(team1_result-team2_result)
print(result)