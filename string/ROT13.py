#https://www.acmicpc.net/problem/11655
import sys
from collections import deque,Counter
input = sys.stdin.readline

array=list(input().rstrip())
result=[]
#음.. 26으로 나눠서 나머지로 계산하는방식으로 해보는게 가장먼저 떠오르네요.근데 소문자도 포함이라 좀애매한데.
#소문자랑 대문자랑 따로 나눠서 계산하는방식으로 해볼까? 더나은방식이뭐가있지?
#생각해보니까 일단 영어가 26글자니까, 만일 13을 더했을때 한계점을 넘으면 빼면되는거아닌가? 안넘으면 더하고?
#예시로 A는 97인가 그러고 Z는 123인가 그러니까. A로는 123을 안넘으니 13을 더하고, Y일경우에는 13을 뺴면될듯?
for i in range(len(array)):
    
    if array[i].isalpha():
        
        if array[i].isupper():  #만일 대문자이면?
            
            if ord(array[i])+13 <= 90:
                result.append(chr(ord(array[i])+13))
            else:
                result.append(chr(ord(array[i])-13))
        else:
            if ord(array[i])+13 <= 122:
                result.append(chr(ord(array[i])+13))
            else:
                result.append(chr(ord(array[i])-13))
    else:
        result.append(array[i])
print("".join(result))