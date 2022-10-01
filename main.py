import sys
from collections import deque
input = sys.stdin.readline
#array = deque()
#모든 소괄호는 짝이있다
#괄호는 1ㄷ1 매칭이된다.
#짝을 이룰때, 그사이 문자열도 균형이잡혀야한다???
#.이 찍이면 입력종료

def solution(arr):
    sum =0      #[] 판별
    aum = 0     #() 판별
    for i in arr:
        if i == "(":
            aum +=1
        elif i == ")":
            if (aum <= 0):  #만약 ( 이게없을때 )나오면 리턴
               return 0
            if (sum >=1) and (aum <=0):   #만약 [이게 호출된상태에서 ) 나오면 리턴인데.
                return 0    #호출될수도있지 시발 ㅋㅋ
            aum -=1
        if i == "[":
            sum +=1
        elif i =="]":
            if (sum <= 0):
                return 0
            if (aum >=1)and (sum <=0):   #만일 (이게 호출된상태에서 ] 나오면 리턴.
                return 0    #]
            sum -=1
    if (aum == 0 )and(sum ==0):
        return 1
    else:
        return 0
    
            
while True:
    array=[]
    A = input().rstrip()
    if A ==".":
        break
    for i in range(len(list(A))):
        array.append(A[i])
    sol=solution(array)
    if sol==0:
        print("no")
    elif sol==1:
        print("yes")
    
    