#https://www.acmicpc.net/problem/1912
import sys
from collections import deque,Counter
input = sys.stdin.readline
# n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 수는 한 개 이상 선택해야 한다.

# 예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이 된다.

# 입력
# 첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

# 출력
# 첫째 줄에 답을 출력한다.

N=int(input())
array=list(map(int,input().split()))
compare,negative,now=[],[],[]
i,result,j=0,0,0
while i<N:
    if array[i]>0:      #양수일경우 더하기.
        now.append(array[i])
    else:               #음수일경우 비교
        negative.append(array[i])
        j=i+1
        while j<N:
            if array[j]>0:
                compare.append(array[j])
            else:
                break
            j+=1
    result=max(sum(compare),sum(now)+result,sum(compare)+result+sum(negative))
    compare,negative,now=[],[],[]
    if j>0:
        i=j
        j=0
    else:
        i+=1
print(result)