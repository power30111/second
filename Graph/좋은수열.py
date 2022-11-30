#https://www.acmicpc.net/problem/2661
import sys
from collections import deque
input=sys.stdin.readline

N=int(input())  #수열의 길이.. 
array=[[],[2,3],[1,3],[1,2]]
now_number=[1]
def check(now_number):
    print(now_number)
    return
        
def DFS(number):
    now_number.append(number)
    
    if len(now_number)==N:     
        check(now_number)
        now_number.pop()
        return
    for i in array[now_number[len(now_number)]]:
        number=i
        DFS(number)
        now_number.pop()
