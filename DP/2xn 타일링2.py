import sys
from collections import deque,Counter
input = sys.stdin.readline

N=int(input())
arr=[0,1,3]

for i in range(3,N+1):
    arr.append(arr[i-1]+arr[i-2]*2) #세로일때는 f(n-1)과 겹친다. f(n-2)*2 는 2x1짜리 가 있는거랑 2x2짜리가 있는거랑
                                    #동일하게 자리를 차지하지떄문에 f(n-2)를 2번 해준다..
print(arr[N]%10007)