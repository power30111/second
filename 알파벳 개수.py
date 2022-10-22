#https://www.acmicpc.net/problem/10808
import sys
from collections import deque,Counter
input = sys.stdin.readline

array=list(input().rstrip())
counter = Counter(array)
for i in range(97,97+26):
    if chr(i) in array:
        print(counter[chr(i)],end=" ")
    else:
        print("0",end=" ")