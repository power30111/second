#https://www.acmicpc.net/problem/1463
import sys
from collections import deque
input = sys.stdin.readline

#입력을 받으면 그입력을 1로만드는 최소연산값을 계산한다.
#X가 3으로 나누어 떨어지면, 3으로 나눈다.
#X가 2로 나누어 떨어지면, 2로 나눈다.
#1을 뺀다.              이러한 3개의 연산만을 이용하여 최소연산을 계산한다.
N = int(input())
array=deque()
array=[0]*(N+1)

for i in range(2,N+1):
    array[i] = array[i-1]+1     #그전꺼에서 1을 빼서 계산하였다는 가정을 먼저해본다..
                #단순하게 10을 기준으로 array[9]->2이므로 array[10-1]->3 이라는뜻. 어렵다
    if i% 2==0: #2로 나눠질경우 1빼서 계산한게 더적어? 아니면 여기서 계산한게 더적어?
        array[i] = min(array[i],array[i//2]+1)  
    if i% 3==0: #3로 나눠질경우 1빼서 계산한게 더적어? 아니면 여기서 계산한게 더적어???
        array[i] = min(array[i],array[i//3]+1)
print(array[N])
print(array)