#https://www.acmicpc.net/problem/15990
import sys
from collections import deque,Counter
input = sys.stdin.readline

arr=[0]*4
arr[0],arr[1],arr[2],arr[3]=[0,0,0],[1,0,0],[0,1,0],[1,1,1]
for i in range(4,100001):           #1번째= 2+3     2번쨰 1+3  3번째 1+2
    arr.append([(arr[i-1][1]+arr[i-1][2])%1000000009,
                (arr[i-2][0]+arr[i-2][2])%1000000009,
                (arr[i-3][0]+arr[i-3][1])%1000000009])
T=int(input())
for i in range(T):
    print(sum(arr[int(input())])%1000000009)

#이게 왜 1000000009를 다 해줘야만 시간초과가 안날까요? 아무래도 숫자가 너무 커져서 그런걸까요?