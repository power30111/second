#https://www.acmicpc.net/problem/1935
import sys
from collections import deque,Counter
input = sys.stdin.readline

array=list(input().rstrip())
stack=[]
result=[]
i=0

while i <len(array):
    
    if array[i].isalpha():
        result.append(array[i])
        i+=1
    else:
        if array[i]=="(":
            while array[i]!=")":
                if array[i].isalpha():
                    result.append(array[i])
                    i+=1
                else:
                    result.append(array[i])
                    i+=1
        else:
            stack.append(array[i])
            i+=1
    #모르겟음 ㅋㅋ