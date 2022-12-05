#https://www.acmicpc.net/problem/11279
import sys
import heapq
from collections import deque
input=sys.stdin.readline

N=int(input())
heap=[]
for i in range(N):
    A=int(input())
    if A==0:
        if len(heap)>0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,[-A,A])
        
#heapq 를 사용하면 최소 힙을 기준으로 만들어진다.
#그러므로 -A를 사용한 리스트를 사용함으로써 heap에 저장되는 순서를 바꾼다.