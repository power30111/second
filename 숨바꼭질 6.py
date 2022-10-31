#https://www.acmicpc.net/problem/17087
import sys
from collections import deque
input = sys.stdin.readline
# 수빈이는 동생 N명과 숨바꼭질을 하고 있다. 수빈이는 현재 점 S에 있고, 동생은 A1, A2, ..., AN에 있다.
# 수빈이는 걸어서 이동을 할 수 있다. 수빈이의 위치가 X일때 걷는다면 1초 후에 X+D나 X-D로 이동할 수 있다. 
# 수빈이의 위치가 동생이 있는 위치와 같으면, 동생을 찾았다고 한다.
# 모든 동생을 찾기위해 D의 값을 정하려고 한다. 가능한 D의 최댓값을 구해보자.
N,S=map(int,input().split())    #N=동생 수 S=현재위치
array=list(input().split())     #동생들 위치 .
distance,result=[],[]
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
for i in array:
    distance.append(abs(int(i)-S))
if N==1:
    print(*distance)
    exit(0)
for i in range(N-1):
    result.append(gcd(distance[i],distance[i+1]))
print(min(result)) 