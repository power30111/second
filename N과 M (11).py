#https://www.acmicpc.net/problem/15665

N,M = map(int,input().split())

array=sorted(list(map(int,input().split())))
result={}
def DFS(a,b,array):
    #a=현재 잡고있는 숫자,b=수열 크기
    if b>=M:
        result[tuple(a)]=True
        return
    for i in array:
        a.append(i)
        DFS(a,b+1,array)
        a.pop()
        
DFS([],0,array)
for i in result.keys():
    print(*i)