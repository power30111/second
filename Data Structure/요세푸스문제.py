#https://www.acmicpc.net/problem/1158
import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())  #N= 사람들 수 M= M번째사람을 제거 출력=없어지는 순서.
#시간 2초 메모리 256MB
#3 [1,2,4,5,6,7]
#6 [1,2,4,5,7]
#2 [1,4,5,7]
#7 [1,4,5]
#5 [1,4]
#1 [4]
#4  
array =deque()
for i in range(1,N+1):
    array.append(i)
print("<",end="")
#여기 는 내가 짠 코드
for i in range(N):  #3개까지 뽑고 3번쨰거 print후 2개를 매열맨뒤로.
    for j in range(M-1):
        array.append(array.popleft())
    if i == N-1:
        print(array.popleft(),end=">")
    else:
        print(array.popleft(),end=", ")
#deque 에서 rotate를 사용해서 그걸 print(popleft())로 한거가 시간이 엄청작다.
#append O(1)인데 popleft()가 O(1) 아닌가?? deque가 좋은이유가 O(1)이라서가 아닌가?
#아니면 big O 에서 상수부분이 차이가나서그런가.. if문도 해서 그런가?음..
#위 코드는 메모리 32420KB 3204ms가 나왔는데 아래코드는 32428KB 92ms이다.
#여기는 참고한 코드
for i in range(N-1):
    array.rotate(-(M-1))
    print(array.popleft(),end=", ")
print(array[0],end=">")