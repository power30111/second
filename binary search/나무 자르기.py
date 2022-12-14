#https://www.acmicpc.net/problem/2805
import sys
from collections import deque
input=sys.stdin.readline          

N,M = map(int,input().split())

array = list(map(int,input().split()))
array.sort()
start,end = 0,1000000000
while start<=end:
    mid = (start+end)//2
    S=0
    for i in range(len(array)):
        if int(array[i]) < mid:
            pass
        else:
            S+=int(array[i])-mid
    if S > M:
        start= mid+1
    elif S < M:
        end = mid-1
    else:
        start= mid+1
print(end)
#거의 2일동안 끙끙 앓은 문제입니다.. 2진탐색으로 풀어야한다는건 알았으나 구현에 시간이 오래걸렸습니다..
#결국 백준에 문제를 물어보고 반례를 본뒤 현상을 고치는 방식으로 해결했습니다.
#아직 2진탐색을 구현하는것에는 어려움이 있어서 앞으로도 계속 풀어봐야할것같습니다......................
