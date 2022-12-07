#https://www.acmicpc.net/problem/2580
import sys
from collections import deque
input=sys.stdin.readline

array=[[]for i in range(9)] #스도쿠 판
empty=[]
for i in range(9):
    array[i]=list(map(int,input().split()))    #스도쿠 판 값 넣어주기.
    for j in range(9):
        if array[i][j]==0:
            empty.append([i,j])
#스도쿠 특성상 가로줄 검사와 세로줄 검사, 그리고 내가 속한 3*3 내부에서 숫자중복검사를 시행한다.
#만일 가다가 검사가 안될경우 돌아와야함.

def col_check(x:int,y:int,number):
    for i in range(9):
        if number==array[x][i]:
            return False
    return True

def row_check(x:int,y:int,number):
    
    for i in range(9):
        if number==array[i][y]:
            return False
    return True

def group_check(x:int,y:int,number):
    x=x//3*3
    y=y//3*3
    for i in range(3):
        for j in range(3):
            if number==array[x+i][y+j]:
                return False
    return True

def DFS(N):
    if N==len(empty):
        for i in range(9):
            print(*array[i])
        exit(0)
    
    for i in range(1,10):
        x=empty[N][0]
        y=empty[N][1]
        if row_check(x,y,i) and col_check(x,y,i) and group_check(x,y,i):
            array[x][y]=i
            DFS(N+1)
            array[x][y]=0
            
DFS(0)
