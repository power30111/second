#https://www.acmicpc.net/problem/15810
import sys
input=sys.stdin.readline

N,M=map(int,input().split())
array=list(map(int,input().split()))
result=0
a,b=0,max(array)*M
while a <= b:
    time = (a+b)//2
    cnt=0
    for i in array:
        cnt+= time//i
    if cnt >= M:
        result=time
        b=time-1
    else:
        a=time+1
print(result)
