#https://www.acmicpc.net/problem/6588
import sys
from collections import deque
input = sys.stdin.readline

n,m=2,1000000
array=[True]*1000001
Prime=[]*100000
array[1]=False
for i in range(n,m+1):
    j=i*i
    while j<m+1:
        array[j]=False
        j+=i
for i in range(n,m):
    if array[i]:
        Prime.append(i)
ma=len(Prime)
while True:
    T=int(input())
    if T==0:
        break
    i=0
    j=0
    while True:
        if Prime[i]+Prime[j]==T:
            print("{} = {} + {}".format(T,Prime[i],Prime[j]))
            break
        if Prime[j]<T and j<ma-1:
            j+=1
        elif Prime[i]<T and i<ma-1:
            i+=1
            j=i
        else:
            print("Goldbach's conjecture is wrong")
            break