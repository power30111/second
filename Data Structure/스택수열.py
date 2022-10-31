#https://www.acmicpc.net/problem/1874
#원하는주석 Ctrl + /
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
stack = []
result = []
cnt = 0
pos = 'YES'
for i in range(n):
    num = int(input())
    while cnt < num:
        cnt += 1
        stack.append(cnt)
        result.append('+')
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        pos = 'NO'
        print(pos)
        break
if pos == 'YES':
    for i in result:
        print(i)
   #아니 대충 이렇게 해야지~ 햇는데 pypy 아니면 시간초과. pypy3로 내더라도 시간소요가 어마무시함..

#도윤기가 짠코드

import sys
input = sys.stdin.readline
n = int(input())
arr = []
stack = []
ans = []
for i in range(n):
    arr.append(int(input()))

cur = 1
for i in range(len(arr)):
    if not stack:
        ans.append('+')
        stack.append(cur)
        cur += 1
    if stack and stack[-1] < arr[i]:
        while stack[-1] < arr[i]:
            stack.append(cur)
            cur += 1
            ans.append('+')
        stack.pop()
        ans.append('-')
    elif stack and stack[-1] > arr[i]:
        while stack[-1] > arr[i]:
            stack.pop()
            ans.append('-')
    elif stack and stack[-1] == arr[i]:
        stack.pop()
        ans.append('-')

if not stack:
    for i in ans:
        print(i)
else:
    print('NO')