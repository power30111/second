#https://www.acmicpc.net/problem/1931
import sys
from collections import deque
input=sys.stdin.readline
N=int(input())

time =[[0]*2 for _ in range(N)]
for i in range(N):
    A,B=map(int,input().split())
    time[i][0]=A
    time[i][1]=B

time.sort(key = lambda x:(x[1],x[0]))

cnt=1

end_time=time[0][1]
for i in range(1,N):
    if time[i][0]>=end_time:
        cnt+=1
        end_time=time[i][1]
    
print(cnt)