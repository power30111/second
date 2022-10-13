#https://www.acmicpc.net/problem/1158
import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())  #N= 사람들 수 M= M번째사람을 제거 출력=없어지는 순서.
#시간 2초 메모리 256MB
#3 [1,2,4,5,6,7]
#6 [1,2,4,5,7]
#2 [1,4,5,7]
#7 [1,4,5]
#5 [1,4]
#1 [4]
#4  
for i in range(N):
    
