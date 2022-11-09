#https://www.acmicpc.net/problem/11052
import sys
from collections import deque
input = sys.stdin.readline

N=int(input())                  #카드 개수
P=[0]+list(map(int,input().split()))        #카드별 가격
arr=[0]*(N+1)

for i in range(1,N+1):
    for j in range(1,i+1):
        arr[i]=max(arr[i],arr[i-j]+P[j])
print(arr[N])
