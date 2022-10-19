#https://www.acmicpc.net/problem/17299
import sys
from collections import deque,Counter
input = sys.stdin.readline

N = int(input())
array=list(input().split())
max_num=[]
result=[0 for i in range(N)]
counter=Counter(array)
for i in range(N-1,-1,-1):
    now_number=array[i]
    if not max_num:
        max_num.append(now_number)
        result[i]=-1
    if int(counter[now_number])<int(counter[max_num[-1]]):
        result[i]=max_num[-1]
        max_num.append(now_number)
    else:
        while max_num:
            if int(counter[now_number]) < int(counter[max_num[-1]]):
                result[i] = max_num[-1]
                max_num.append(now_number)
                break
            max_num.pop()
            if not max_num:
                result[i]=-1
                max_num.append(now_number)
                break

print(*result)
#이건 오큰수문제를 푼뒤에 푼거라 비슷한 구조로 풀어서 해결함.
#단지 처음으로 counter 써봐서 조금걸림 O(N)으로 각 문자마다 문자열에서의 횟수를 반환.