#https://www.acmicpc.net/problem/10430
import sys
from collections import deque
input = sys.stdin.readline

A,B,C = map(int,input().split())
#첫째줄(A+B)%C 둘쨰줄 ((A%C)+(B%C))%C 셋째줄 (A*B)%C 넷째 ((A%C) × (B%C))%C 를 한줄씩 출력.

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

#ㅎㅎ;