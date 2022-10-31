#https://www.acmicpc.net/problem/10809
import sys
from collections import deque,Counter
input = sys.stdin.readline

array= list(input().rstrip())
result=[-1]*26
for i in range(len(array)):
    
    if result[ord(array[i])-97]=="-1":
        result[ord(array[i])-97]=i
print(*result)