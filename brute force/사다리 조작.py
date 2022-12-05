#https://www.acmicpc.net/problem/15684
import sys
from collections import deque
input=sys.stdin.readline

def solve(added, num):
    global minans
    if added >= minans:
        return
    if check():
        minans = added
        return
    for idx in range(num+1, len(candidates)):
        i, j = candidates[idx]
        if lines[i][j-1] == 0 and lines[i][j+1] == 0:
            lines[i][j] = 1
            solve(added + 1, idx)
            lines[i][j] = 0
            
    
def check():
    for i in range(1, N+1):
        now = i
        for j in range(1, H+1):
            if lines[j][now] == 1:
                now += 1
            elif lines[j][now-1] == 1:
                now -= 1
        #print(i,'->' ,now)
        if i != now:
            return False
    return True
                
N, M, H = map(int, input().split())
lines = [[0 for _ in range(N+1)] for _ in range(H+1)]
candidates = []
minans=4
for _ in range(M):
    t1, t2 = map(int, input().split())
    lines[t1][t2] = 1
for i in range(1, H+1):
    for j in range(1, N):
        if lines[i][j] == 0 and lines[i][j-1] == 0 and lines[i][j+1] == 0:
            candidates.append([i, j])
solve(0, -1)
print(minans if minans < 4 else -1)


# N,M,H=map(int,input().split())  #N=세로선 M=가로선의 개수 H=세로선 당 놓을수있는 가로선의 개수
# array=[[False]*(N+1) for _ in range(H+1)]
# for i in range(M):
#     A,B=map(int,input().split())
#     array[A][B]=True    

#     #선을 양쪽에 이어보고싶은데 그러면 내가 확인하는선이 왼쪽으로 갈지 오른쪽으로 갈지 모르겟음.
#     #array[A][B]에서 A는 행번호를 의미 B는 열번호를 의미한다 (행=가로)(열=세로)
# def check():
#     for i in range(1,N+1):
#         vertical,width=1,i          #현재 높이 위부터 내려오는걸로다가ㅇㅇ
#         while vertical<=H:          #한칸씩 검사한뒤 아래로 내려감 == vertical+=1
            
#             if array[vertical][width]==True:
#                 width+=1
#                 vertical+=1
#             elif array[vertical][width-1]==True:
#                 width-=1
#                 vertical+=1
#             else:
#                 vertical+=1
#         if i!=width:
#             return False
#     return True

# def DFS(cnt,A,B):
#     global ans
#     if ans<=cnt or cnt==3:
#         return
#     if check():
#         ans=min(ans,cnt)
#         return
#     for i in range(A,H):
#         if i ==A:
#             k=B
#         else:
#             k=0
#         for j in range(k,N):
#             if array[i][j]==False:
                
#                 array[i][j]=True
#                 DFS(cnt+1,i,j+2)
#                 array[i][j]=False
# ans=4
# if M == 0:
#     print(0)
#     exit()
# DFS(0,1,1)
# if ans<=3:
#     print(ans)
# else:
#     print(-1)
# #왜 안되었을까? 나중에 다시 코드를 보며 분석해보자.