#https://www.acmicpc.net/problem/1107
import sys
from collections import deque   #deque
from itertools import permutations
#input = sys.stdin.readline

want = int(input())                 #내가 원하는 채널번호
M = int(input())
array=[]
if M != 0:         
    array=list(map(int,input().split()))    #버튼누를수 없는거
count=abs(100-want)     #일단 먼저 100부터 세는거를 count에 입력.
for i in range(1000000):         #간단하게 정할수있는채널에서 위아래로 50만씩 검사.
    now_number = str(i)                  #반례를 통해 알게됨.ex) 500,000 5 12345 일경우. 600000만에서 
                                # 내려가는게 99999에서 올라가는것보다 빠르다.
    for j in range(len(now_number)): #i의 크기만큼(10의자리 100의자리를 구분하기위함. )
        
        if int(now_number[j]) in array:  #만일 i에서 array가 들어있다면
            break               #그건 정답이 될수없으므로 패스
        elif j == len(now_number) -1:    #이부분은 위에서 now_num를 다검사햇는데 없는숫자로만 이루어져있을경우
            count = min(count,abs(int(now_number)-want)+len(now_number))  
            #min()함수로 절대값과 현재최소값 비교하여 최소값 갱신.
print(count)

#브루트 포스로 풀게되었다. 시도해본 것으로는 중복순열, 그리디 알고리즘처럼 각숫자마다 가장가까운것 찾아보기.
#결국 뭔지 모르겟어서 브루트 포스로 대강짜봄.그래서인지 시간이 많이걸린다.