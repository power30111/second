#https://www.acmicpc.net/problem/9093
import sys
from collections import deque   #deque
from itertools import permutations
#input = sys.stdin.readline
#https://www.acmicpc.net/problem/9093
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())    #입력받는 횟수.
array=deque()
A=[]
for i in range(T):
    A=list(input().split())
    for j in range(len(A)):
        for k in range(len(A[j])-1,-1,-1):
            print(A[j][k],end="")
        print(end=" ")
    print()