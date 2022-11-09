#https://www.acmicpc.net/problem/10844
import sys
from collections import deque,Counter
input = sys.stdin.readline

N=int(input())      #계단 길이쓰    100보다작음 

arr=[[0,1,1,1,1,1,1,1,1,1]for i in range(N)]
for i in range(1,N):
    for j in range(1,9):            #0과 9로 끝나는 애들은 특별하게 취급해보자고
        arr[i][j]=arr[i-1][j-1]+arr[i-1][j+1]
    arr[i][0]=arr[i-1][1]
    arr[i][9]=arr[i-1][8]
print(sum(arr[N-1])%1000000000)
