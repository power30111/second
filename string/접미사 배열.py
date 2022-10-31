#https://www.acmicpc.net/problem/11656
import sys
from collections import deque
#input = sys.stdin.readline
result=[]
array=input()

for i in range(len(array)):
    result.append(array[i:len(array)])
print("\n".join(sorted(result)))