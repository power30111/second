#https://www.acmicpc.net/problem/11726
import sys
from collections import deque,Counter
input = sys.stdin.readline

N=int(input())
result=[1,1]
for i in range(2,N+1):
    result.append(result[i-2]+result[i-1])
print(result[N]%10007)
#5까지 그려보니까 1 2 3 5 8... 13 21 34 55 .. 입력예시 9도 55..피보나치 