#https://www.acmicpc.net/problem/17103
import sys
from collections import deque
input = sys.stdin.readline
import sys
from collections import deque
input = sys.stdin.readline
# 골드바흐의 추측: 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.
# 짝수 N을 두 소수의 합으로 나타내는 표현을 골드바흐 파티션이라고 한다. 짝수 N이 주어졌을 때,
#골드바흐 파티션의 개수를 구해보자. 두 소수의 순서만 다른 것은 같은 파티션이다.
# 입력
# 첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 100)가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 N은 짝수이고, 2 < N ≤ 1,000,000을 만족한다.
# 출력
# 각각의 테스트 케이스마다 골드바흐 파티션의 수를 출력한다.
T=int(input())
array=[]
Prime=[True]*(1000000+1)
Prime[1]=False
for i in range(2,1000001):
    if Prime[i]:
        for j in range(i+i,1000001,i):
            Prime[j]=False

for i in range(T):
    num =int(input())
    count=0
    for j in range(2,num//2+1):
        if Prime[num-j] and Prime[j]:
            count+=1
    print(count)