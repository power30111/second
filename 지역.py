import sys
input=sys.stdin.readline

N,M=map(int,input().split())

array=[[]for i in range(N+1)]
for i in range(1,N):
    array[i].append(i+1)
for i in range(M):
    x,y=map(int,input().split())
    array[x].append(y)
print(array)