#https://www.acmicpc.net/problem/1107
import sys
from collections import deque   #deque
from itertools import permutations
#input = sys.stdin.readline

def check_num(arr):
    num=0
    for i in range(len(arr)):
        if len(arr)-i-1 != 0:
            num+=int(arr[i])*(10**(len(arr)-i-1))
        else:
            num+=int(arr[i])
    return num
N = input()    # 원하는채널
M = int(input())    # 고장난 버튼의 개수
chan=[0,1,2,3,4,5,6,7,8,9]   #사용할수있는 채널 목록.
array=input().split()
for i in range(M): 
    chan.remove(int(array[i]))
now = 100
result,now_N=[],[]                  #result =내 결과로 사용할것. now_N= 검사중N의 상태갱신
count=0                             #결국 버튼누른 횟수이므로 count++
want=0
for i in range(len(N)):                 #일단 원하는 숫자만큼 반복한다.
    NN = 5000000                        #대충 큰숫자로 입력(최소값으로써 사용할예정)
    want_num=0                          #
    if int(N[i]) not in chan:           #만일 원하는숫자가 사용할수있는 채널목록에 있다면?
        for j in range(len(chan)):      #채널목록을 다 돌아본다
            number=abs(int(N[i])-int(chan[j]))  #N[i] - chan[j]를 계산해서  number선언
            if NN > number:                     #만일 최소값보다 number가 작다면
                NN = number                     #최소값 변경.
                want_num = int(chan[j])         #want_num은 int(chan[j])를 빼내오기위한 변수인데
        result.append(want_num)          #result에 추가(want_num)
        now_N.append(N[i])               #현재 N검사상태 또한 추가(check_num을 사용하기위함)
        count+=1                         #숫자가 정해졋으므로 버튼을 누른것과 같다. count+=1
    elif len(result)>0:                  #result의 원소가 0보다 클경우?
        if check_num(result) < check_num(now_N):#check_num을 result와 비교해서 아까 N이 더컷으면
            result.append(max(chan))            #사용가능한 버튼중 가장큰수를 result에 추가.
            now_N.append(N[i])                  #현재N상태또한 추가
            count+=1                            #숫자가 정해졋으므로 count+=1
        else:                              #걍 숫자가 더크진않앗으면?
            result.append(int(N[i]))       #그럼 차피 chan에 있으므로 N[i]와 같은값추가.
            now_N.append(N[i])             #현재 N상태또한 갱신
            count+=1                       #이러한 len(result)>0 부분은 800000의 예제를 의식하여
    else:                                  #코드를짯다. 이부분에서 부분순열을 이용한 코드또한 작성해봄.
        result.append(int(N[i]))
        now_N.append(N[i])
        count+=1
        
for i in range(len(result)):                #마지막에 숫자가 다정해졋으면
    if len(result)-i-1 != 0:                # +버튼이나 -버튼을 누른횟수를 N과 result차이를통해구함.
        want+=int(result[i])*(10**(len(result)-i-1))
    else:
        want+=int(result[i])
count+=abs(int(N)-int(want))            
if abs(int(N)-now) < count:                 #만일 100부터 + - 버튼누른게 더 적으면
    count=abs(int(N)-now)                   #100부터 + - 한걸로다가 count하고 종료
    print(count)
    exit()
print(count)