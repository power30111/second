#https://www.acmicpc.net/problem/17298
import sys
from collections import deque
input = sys.stdin.readline

# N = int(input())
# array=input().split()
# discard=[]
# result=[]
# for i in range(len(array)):
    
#     for j in range(i,len(array)):
#         if int(array[i]) < int(array[j]):
#             result.append(array[j])
#             break
#         if j==len(array)-1:
#             result.append("-1")
#             break
# print(" ".join(result))

#-------------------------
#걍 스택구조 이용해서 풀었다.. 훗.. .나란녀석
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
array=list(input().split())
max_num=[]
result=[0 for i in range(N)]
for i in range(N-1,-1,-1):
    now_number=array[i]
    if not max_num:
        max_num.append(now_number)
        result[i]=-1
    elif int(now_number)<int(max_num[-1]):
        result[i]=max_num[-1]
        max_num.append(now_number)
    else:
        while max_num:
            if int(now_number)<int(max_num[-1]):
                result[i]=max_num[-1]
                max_num.append(now_number)
                break
            max_num.pop()
            if not max_num:
                max_num.append(now_number)
                result[i]=-1
                break
print(*result)
