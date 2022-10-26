#https://www.acmicpc.net/problem/10820
import sys
from collections import deque,Counter
#input = sys.stdin.readline
#대문자 소문자 숫자 공백  이렇게 4개의 개수를 공백으로 구분하여 출력.
while True:
    try:
        result=[0,0,0,0] 
        array=list(input())
        if array==[]:
            break
        for i in range(len(array)):
            if array[i].isdigit():
                result[2]+=1
                continue
            elif array[i]==" ":
                result[3]+=1
                continue
            elif array[i].isupper():
                result[1]+=1
                continue
            else:
                result[0]+=1
        print(*result)
    except EOFError:
        break
    
#그 끝나는 시점이 명확하게 나오지않았을경우 . EOFError를 통하여 종료시점을 알잘딱해야함..
#EOF=End of file 이며 파일의 끝을 표현하기위하여 정의한 상수라고한다.