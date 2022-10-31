#https://www.acmicpc.net/problem/9613
import sys
from collections import deque
input = sys.stdin.readline

#GCD= 최대공약수 그니까 주어진 숫자들에서 최대공약수들을 구하고, 그거들의 합을 출력하라 라는 문제입니다.
T=int(input())

for i in range(T):
    array=list(input().split())
    result=0
    for j in range(1,len(array)):
        for k in range(j+1,len(array)):
            C=1
            A,B=int(max(int(array[j]),int(array[k]))),int(min(int(array[j]),int(array[k])))
            while True:
                if C==0:
                    break
                C=A%B
                A=B
                B=C
            result+=A
    print(result)
#이거 맨앞 숫자까지 같이하는게 아니라 숫자개수였음;