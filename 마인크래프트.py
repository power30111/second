#https://www.acmicpc.net/problem/18111
import sys
from collections import deque
input = sys.stdin.readline
arr=deque()
N,M,B=map(int,input().split())
for i in range(N):
    a=input().rstrip().split()
    arr.append(list(a))
max_size = B
for i in range(N):
    for j in range(M):
        max_size+=int(arr[i][j])
max_size= max_size//(N*M)   #최대 높이는 모든 높이//땅넓이 보다 높게나올수없다.
fast_stand=int(max_size)    #가장 빨랏던 층은 초기에 최대 높이로 한다.
fast_time = sys.maxsize     #가장 빠른 시간은 초기에 maxsize로 한다.
for stand in range(max_size,-1,-1):     #가장 높은 층부터 차례대로 한다.
    time=0                              #땅 높이별 걸리는 시간은 2차함수의 꼴을 하고있으므로
    for i in range(N):                  #max_size 보다 큰 높이는 더 클수밖에없음.
        for j in range(M):
           dis_stand = int(arr[i][j])-stand #stand(검사하는 높이)-(현재 높이) = 그차이
           time += dis_stand*2 if dis_stand >0 else -dis_stand
    if fast_time >time:                 #가장 빨랏던 시간보다 더 빠른시간대가 나오면
        fast_time = time                #교체
        fast_stand = stand
    else:                   #아닐경우 그 이후 시간대에서는 더 빠른시간대가 나오지않는다는 뜻
        break               #이므로 이후는 검사하지않는다.
print(fast_time,fast_stand) 
