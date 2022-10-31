#https://www.acmicpc.net/problem/1012
import sys
from collections import deque
input = sys.stdin.readline
def XYZ(a,b):
    if check[a][b]:     #check판에서 좌표 a,b 부분이 True인 땅일경우 상하좌우 체크
        check[a][b]=False
        if array[a+1][b]==1:   #가로 a+1,b 의 좌표
            XYZ(a+1,b)
            check[a+1][b]=False

        if array[a][b+1]==1:
            XYZ(a,b+1)
            check[a][b+1]=False

        if array[a-1][b]==1:
            XYZ(a-1,b)
            check[a-1][b]=False

        if array[a][b-1]==1:
            XYZ(a,b-1)
            check[a][b-1]=False
        return 1
    return 0
def test():
    Sum=0
    for i in range(N):
        for j in range(M):
            a=XYZ(i+1,j+1)
            Sum+=int(a)
    return Sum
#T = test time
#M 밭의 가로길이 N 밭의 세로길이 K배추의 개수 이후로 차례대로 배추가 심어져있는 좌표 입력
#(1,1)의 좌표가 가장 왼쪽위 이다.
T = int(input())
for time in range(T):
    M,N,K = map(int,input().split())
    array=[[0 for col in range(M+2)]for row in range(N+2)]  #새로운 땅세팅
    check=[[False for col in range(M+2)]for row in range(N+2)]
    for i in range(K):
        W,L = map(int,input().split())  #L가로 W 세로
        array[L+1][W+1]=1
        check[L+1][W+1]=True
    result=test()
    print(result)