#https://www.acmicpc.net/problem/1934
import sys
from collections import deque
input = sys.stdin.readline

T= int(input())
def hi(array):
    A=int(max(array))
    B=int(min(array))
    C=1
    while True:
        if C==0:
            break
        C=A%B
        A=B
        B=C
    print(int(array[0])*int(array[1])//A)
    
for i in range(T):
    array=input().split()
    hi(array)
    