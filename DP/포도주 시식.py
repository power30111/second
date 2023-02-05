#https://www.acmicpc.net/problem/2156
import sys
input = sys.stdin.readline
#연속으로 놓여있는 3잔을 모두 마실수없다.

n=int(input())
array=[0]*10000
dp=[0]*10000
for i in range(n):
    array[i]=(int(input()))

#즉 현재 N번쨰의 잔을 마실수 있는 경우는
#n-1 또는 n-2 일터.. 하지만 n-1번쨰가 총총총 술마시며 뛰어왔을수도있다.
# [n-2 + n] or [n-3+n-1+n] 의 경우로 마시겟지.. 

dp[0]=array[0]
dp[1]=array[0]+array[1]
if n<=2:
    print(sum(array))
    exit()
#첫번째랑 두번쨰는 미리 정해주자. 그리고 이후 가능한 경우의수 중 높은숫자걸 선택한다.
#단 array[i-1]을 dp[i-1]로 쓰면 포도주의 양이 복사가 되니 조심하자..
for i in range(2,n):
    dp[i]=max(dp[i-1],max(dp[i-3]+array[i-1]+array[i],dp[i-2]+array[i]))

#연속3잔만 아니면 되는부분이라.. 굳이 포도주양이 0인 곳까지 안가도된다..
#즉 0인 곳을 방문하는게 더 손해인 경우라면 그냥 직전 값을 가져온다
print(max(dp))
