#https://www.acmicpc.net/problem/2089
import sys
from collections import deque
input = sys.stdin.readline
#나누는 수가 양수일경우 abs(now_number) 
#나누는 수가 음수일경우 abs(now_number)+1       여기서 둘다 나머지계산에서는 1과0으로만 이루어져야함.
#ㅅㅂ.. 음수의 나머지 계산을 알아보았다..       ex)-13에서 -2로 나누면 몫=7 나머지 1    7에서 -2로나누면 몫-3 나머지 1
now_number=int(input())
result=[]
if now_number==0:
    print(0)
    exit(0)
while now_number!=1:
    if now_number<0:
        result.append(now_number%2)
        now_number=((now_number//2))*-1
    else:
        result.append(now_number%2)
        now_number=(now_number//2)*-1
if now_number==1:
    result.append(1)
else:
    result.append(0)
print(''.join(map(str,reversed(result))))

#나머지 연산에 대해서 알수있었따..