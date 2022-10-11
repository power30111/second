#https://www.acmicpc.net/problem/1260
import sys
from collections import deque,defaultdict   #deque 딕셔너리
from itertools import permutations
input = sys.stdin.readline
N,M,V = map(int,input().split())
#N=정점의 개수 M= 간선의 개수 V = 시작하는 정점. 모든정점을 다훑고온다.
array=defaultdict(int)
for i in range(M):
    A,B = input().split()
    array[A]+=int(B)
print(array)