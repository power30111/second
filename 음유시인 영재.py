#https://www.acmicpc.net/problem/19948
import sys

sentence = input()              #주어진 문장
N=int(input())                          #스페이스바 사용가능 횟수
keyboard=list(map(int,input().split())) #키보드 사용가능 횟수
title=[]                                #제목

def check(x):
    global N
    if x == ' ':
        if N == 0:
            print("-1")
            return
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
        
for i in sentence:
    x=i[0]
    title.append(x.upper())
    for j in range(1,len(i)):
        x=i[j]
        if x == i[j-1]:
            continue
        check(x)

for i in title:
    check(i)
print(''.join(title))