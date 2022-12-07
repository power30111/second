import sys
from collections import deque,Counter
input = sys.stdin.readline

#위에 import 부분 복사용
#타입힌트 사용하기 ex) A:int=input() ....
알아둬야할 표준 라이브러리 목록.
#itertools      #반복되는 형태의 데이터를 처리하기 위한 기능들 포함 ex)순열(permutations),조합(combination) 등등..
#heapq          #힙(Heap)자료구조를 제공함 ex)우선순위 큐 등등..
#bisect         #이진탐색(Binary Search)기능을 제공한다.
#collections    #덱(deque),카운터(Counter)등등 유용한 자료구조를 제공한다.
#math           #수학적 기능을제공한다. ex)팩토리얼, 제곱근, GCD(최대공약수),LCM(최소공배수), 삼각함수 등등

모든 경우의 수를 고려해야 할때.
순열: -> 서로 다른 n개에서 서로 다른r개를 선택하여 일렬로 나열하는것.
ex) {A,B,C}에서 세개를 선택하여 나열하는경우.=ABC,ACB,BAC,BCA,CAB,CBA
순열의 수는 nPr => n*(n-1)*(n-2)...*(n-r+1)

조합: -> 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는것.
ex) {A,B,C}에서 순서를 고려하지 않고 두 개를 뽑는 경우=AB,AC,BC
조합의 수는 nCr => n*(n-1)*(n-2)...*(n-r+1)/r! 

#파이썬에서 함수주석은 """ 로 시작한다.

########################################
https://cafe.naver.com/startdevelopercareer?iframe_url_utf8=%2FArticleRead.nhn%3FreferrerAllArticles%3Dtrue%26clubid%3D30372458%26articleid%3D6
1. 휴식이 끝났을 때 마음이 안정되어있어야한다.
ex)휴식했는데도 긴장이 풀리지않거나, 열이받고 초조해진다? ->lol overwatch.
2.자율성이 보장되어있는 휴식이여야한다.
ex)내 선택권이있는 부담없는 휴식을 취하여야한다.
3.몰입하는것이 좋다.
ex) 무엇인가를 열심히하는것도 좋은 휴식이될수있다.
그런데 집중을 하는것도 안하는것도 아닌 상태(인스타본다거나, 유튜브쇼츠 본다거나)
즉 집중을 오지게 한다거나, 아예 안하는 상태여야한다(멍)
*4. 거리두기?
ex)내가 하던 일과 거리두기가 필수이다. 내 일과는 완전히 별걔의 휴식을 취하는것이
가장 좋은 휴식이다. 거리두기가 되지않은 휴식은 진정한 휴식이 아니다.

