#https://www.acmicpc.net/problem/1406
import sys
from collections import deque
input = sys.stdin.readline

#L=커서왼쪽한칸 D=커서오른쪽한칸 B=커서왼쪽문자삭제 P $= $라는 문잘르 커서왼쪽에 추가.

array= list(input().rstrip())  #기본 문자열
cusor=[]
M = int(input())    #입력할 명령어의 개수
for i in range(M):
    com=input().split()
    if com[0] == "L":
        if array:
            cusor.append(array.pop())
    elif com[0] =="D":
        if cusor:
            array.append(cusor.pop())
    elif com[0] =="B":
        if array:
            array.pop()
    else:
        array.append(com[1])
print("".join(array+list(reversed(cusor))))
