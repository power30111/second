#https://www.acmicpc.net/problem/2630
import sys
from collections import deque
input=sys.stdin.readline

N=int(input())      #종이의 가로 세로 길이(정사각형임)
array=[[]for i in range(N+1)]
white,blue=0,0
for i in range(N):
    array[i]+=input().split()
# 1. 현재 사각형이 1또는 0으로 이루어져있는지에대해서 확인한다.
# 2. 만일 맞을경우 1을 리턴하고 넘어간다. 아닐경우 다시 4등분을 한뒤 검사한다.
def check(x:int,y:int,N:int):
    """_주어진 사각형 내부탐색함수_

    인자들:
        x (int): _현재 x좌표
        y (int): _현재 y좌표
        N (int): _현재 보고있는 사각형의 크기

    반환값:
        _bool_: 하나의 색깔로 가득차있으면 True 아니면 False
    """
    standard=array[x][y]
    
    for i in range(x,x+N):
        for j in range(y,y+N):
            if standard!=array[i][j]:
                return False
    return True

def rec(array:list,x:int,y:int,N:int): 
    """ 색종이만들기용 재귀함수

    Args:
        array (list): 입력으로 주어진 정사각형을 이루는 리스트
        x (int): 현재 x좌표
        y (int): 현재 y좌표
        N (int): 현재 보고있는 정사각형의 크기
    """
    global white,blue
    if check(x,y,N):
        if array[x][y]=='0':
            white+=1
            return
        else:
            blue+=1
            return
    rec(array,x,y,N//2)
    rec(array,x+N//2,y,N//2)
    rec(array,x,y+N//2,N//2)
    rec(array,x+N//2,y+N//2,N//2)
rec(array,0,0,N)
print(white)
print(blue)
