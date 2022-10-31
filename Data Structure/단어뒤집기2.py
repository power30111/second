#https://www.acmicpc.net/problem/17413
import sys
from collections import deque
input = sys.stdin.readline

array=list(input().rstrip())    #문자열 입력받기.
i=0                             #현재 검사하는 문자번호
start=0                         
while i<len(array):             #이 문자열을 하나하나 체크.
    if array[i]=="<":           #만일 <가 나오면
        i+=1                    #그건 건드리지않는다.(정상출력)
        while array[i]!=">":    #>가 나올떄까지
            i+=1                #계속해서 건드리지않는다.
        i+=1                    #탈출시 >까지 넘어간다.
    elif array[i].isalnum():    #만일 < , > 가 아니고 문자라면
        start=i                 #여기부터 역으로 출력해야하므로 시작지점 저장
        while i < len(array) and array[i].isalnum():#문자열 크기보다 작고 숫자문자면?
            i+=1                        #여기도 i+=1을 해준다.start~i까지 reverse 해준다.
        arr=array[start:i]              #array에서 start~i 까지의 배열을 arr에 저장
        arr.reverse()                   #arr에 저장된 배열을 reverse 한다.
        array[start:i]=arr              #array에서[start:i]까지 를 arr에 저장된 배열로 변경한다.
    else:                               #만일 숫자문자도 아니고 <>도 아닌, 스페이스바 " " 빈문자열일경우
        i+=1                            #걍 넘어감~
print("".join(array))                   #array에 있는 원소들을 문자열로 출력한다.join()을 통해.
    