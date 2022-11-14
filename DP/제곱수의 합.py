#https://www.acmicpc.net/problem/1699
import sys
from collections import deque,Counter
input = sys.stdin.readline

N=int(input())
DP=[]
for i in range(N+1):
    DP.append(i)
for i in range(1,N+1):
    for j in range(1,i):
        if j*j>i:
            break
        if DP[i]>DP[i-j*j]+1:
            DP[i]=DP[i-j*j]+1
            
print(DP[N])
#.. 처음DP[i]는 1로만 구성되어있는 걸로 가정하고 시작한다.
#0,1,2,3 까지는 제곱수가 없으나 4부터 2*2로 나타낼수있다.
#DP[4-2*2]일경우 (그니까 자연수N의 제곱에 해당하는 수들은 딱 맞아떨어지므로 1이다.)
#제곱에 사용한 최소항이 1이므로 +1을 해준다.
#ex 11일경우 DP[11]= 11일테고, DP[11-1*1]+1,DP[11-2*2]+1,DP[11-3*3]+1까지 비교해서
#최소값을 저장한다. 이경우 DP[11-3*3]+1이 가장 짧다.
#753의 경우? 항상 최대항으로 계산해보면 27*27+4*4+2*2+2*2가된다.
#DP[753-1*1]+1...부터 시작해서 DP[753-25*25]였을경우 DP[128]이였을때가 가장 적었다는것을
#알아내서 DP[128]=8*8+8*8 즉 3개의 항이다. DP너무 어려운데ㅎ;