#https://www.acmicpc.net/problem/1927
import sys
import heapq
from collections import deque
input=sys.stdin.readline

N=int(input())
heap=[]
#x=0 이라면 배열에서 가장 작은 값을 출력 x=자연수라면 배열에 x란 값을 추가.

for i in range(N):
    A=int(input())
    if A==0:
        if len(heap)>0:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,A)
        
#heappop(list)=> 리스트내 가장 작은 원소를 뽑는다
#heappush(list,element)=> 원소를 list에 알아서 잘 넣어준다.