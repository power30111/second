#https://www.acmicpc.net/problem/10799
import sys
from collections import deque
input = sys.stdin.readline

array=list(input())
i,result,N=0,0,0
for i in range(len(array)):
    
    if array[i]=="(":
        N+=1
        i+=1
    elif array[i]==")":
        if array[i-1]==")":
            N-=1
            result+=1
            i+=1
        else:
            N-=1
            result+=N
            i+=1
print(result)
#닫는점은 무조건나오기떄문에. 예전에 풀엇던 ()괄호정리하는 문제를 떠올리며 풀었다.
#간단하게 문제풀이를 설명하면, 처음부터 끝까지 문자하나하나 검사하는데, 괄호가"(" 이게 나올경우 
#자를수있는 막대의 크기도 늘어난다고 생각하여 N+1을 해주었고, 괄호가")"이게 나올경우에서는
#전에 ")" 이게 나온경우에는 막대의 개수가 줄어들지만 나머지 막대크기도 남으므로 result+=1 개수는 N-=1해주었다.
#만일 전에 ")" 이게 안나온 경우에는 걍 레이저로 자르는 경우이므로 막대의 개수 N만큼 result에 더해준다.
#for 문인데 i를 늘리는이유는 걍 첨에 while 써서 흔적이남앗다...없어도 ㄴ상관일듰??