#https://www.acmicpc.net/problem/2805
import sys
from collections import deque
input = sys.stdin.readline
def QQ(arr,N,now,M):
    result =0
    for i in range(N):
        if int(arr[i])-now >=M:
            result+=int(arr[i])-now  #나무 크기에서 현재톱길이만큼 자름. 자른만큼 result+
    return int(result)
array=deque()
N,M = map(int,input().split())      #N 나무의수 M가져갈려는 나무의 길이
array = input().split()
array.sort()
start=0
end=int(array[-1])+1
II = -1
while True:
    i = (start+end)//2
    result=QQ(array,N,i,M)
    print("시작{} 중간{} 끝{} result값{}".format(start,i,end,result))
    if result >= M and start<=end:
        start=i+1
        if II < i:
            II = int(i)
    elif result < M and start<=end:
        end=i-1
        if II < i:
            II = int(i)
    else:
        print(II)
        break

        