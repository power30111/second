#https://www.acmicpc.net/problem/1373
import sys
from collections import deque
input = sys.stdin.readline

array=list(input().rstrip())
j=0
result=deque()
cal=[0,0,0]
if len(array)==1:
    print(array[0])
    exit(0)
for i in range(len(array)-1,-1,-1):
    if j==2:
        cal[j]=int(array[i])
        result.appendleft(cal[2]*4+cal[1]*2+cal[0])
        cal=[0,0,0]
        j=0
    else:
        cal[j]=int(array[i])
        j+=1
if 1 in cal:
    result.appendleft(cal[2]*4+cal[1]*2+cal[0])
while result:
    print(result.popleft(),end="")
#------------------------------------------------------------------------
n = int(input(),2)
n = oct(n)
print(n[2:])
#??? 이건머지 ㅋㅋ  int에 인자가 두개 들어갈수있다는건 첨알았네. default 가 10이라 10진수였던거 ㄷㄷ;