#https://www.acmicpc.net/problem/19948
import sys

sentence = list(input())              #주어진 문장
N=int(input())                          #스페이스바 사용가능 횟수
keyboard=list(map(int,input().split())) #키보드 사용가능 횟수
title=[sentence[0].upper()]                                #제목
def check(x):
    global N
    if x == ' ':
        if N == 0:
            print("-1")
            exit()
        else:
            N-=1
            return
    else:
        if x.isupper():
            x=ord(x)-65
            if keyboard[x]!=0:
                keyboard[x]-=1
                return 
            else:
                print("-1")
                exit()
        else:
            x=ord(x)-97
            if keyboard[x]!=0:
                keyboard[x]-=1
                return
            else:
                print("-1")
                exit()
x=sentence[0]
check(x)
for i in range(1,len(sentence)):
    y = sentence[i]
    if y == x:  #전꺼랑 다르면
        continue
    check(y)            #check
    if x == ' ':
        title.append(y.upper())
    x=y

check(title[0])

for i in range(1,len(title)):
    x=title[i]
    if x == title[i-1]:
        continue
    check(x)

print(''.join(title))