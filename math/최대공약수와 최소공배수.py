#https://www.acmicpc.net/problem/2609
import sys
from collections import deque
input = sys.stdin.readline

#두개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

array=input().split()
A=int(array[0])
B=int(array[1])
C=1

while True:
    
    if C==0:
        break
    C=A%B
    A=B
    B=C
B=(int(array[0])*int(array[1]))//A
print(A,B)
#유클리드 호제법