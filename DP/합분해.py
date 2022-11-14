#https://www.acmicpc.net/problem/2225
import sys
from collections import deque,Counter
input = sys.stdin.readline
#타입힌트 사용하기 ex) A:int=input() ....
N,K=map(int,input().split())
#0~N까지 수중에서 K개만큼 사용해서 N이 되는 경우의 수를 구하라.
#ex 20 2 => 1+19,2+18,3+17...19+1 에서 0+20 까지 하면 20개+1개 여기서 0+0+ 이런것도 가능한건가?
#만일 가능하다면 6 4 의 예제의 경우 6 3 의 경우 랑 6 2 의 경우 6 1 의 경우까지 다더하고 그이후에
# 6 4 의 경우까지 해야겟네요? 그렇다면 20 2도 20 2의 경우에 20 1의 경우까지 합쳐서 21개 인거네.
DP=[[i for i in range(K+1)]for j in range(N+1)]
for i in range(1,K+1):
    DP[1][i]=i
for i in range(1,N+1):
    DP[i][1]=1
for i in range(2,N+1):
    for j in range(2,K+1):
        DP[i][j]=(DP[i][j-1]+DP[i-1][j])%1000000000
print(DP[N][K])
#K가 1일경우 N은 N밖에 만들수없으므로 1이다.
#N이 1일경우 N을 만들수있는 경우의 수는 N과 같다.
#임의의 숫자 A+B=N으로 나타낼수있다..https://hongjw1938.tistory.com/63참고.