#https://www.acmicpc.net/problem/10824
import sys
from collections import deque
input=sys.stdin.readline      

A,B,C,D = input().split()

print(int(A+B)+int(C+D))