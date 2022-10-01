#https://www.acmicpc.net/problem/1966

import sys
from collections import deque

input=sys.stdin.readline #파이썬 입출력 느려터져서 설정함 ㅇㅇ
array=deque()            #일단 array는 기본적으로 deque로 활동하자.
D=deque()
t = int(input())        #총 반복횟수

for i in range(t):
    N,M=map(int,input().split())
    array = deque(list(map(int,input().split())))
    count =0
    while array:
        best = max(array)
        front = array.popleft()
        M -= 1

        if best == front:
            count +=1
            if M < 0:
                print(count)
                break
        else:
            array.append(front)
            if M < 0:
                M = len(array) -1
