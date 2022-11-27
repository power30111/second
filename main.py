import sys
from collections import deque,Counter
input = sys.stdin.readline

#위에 import 부분 복사용
#타입힌트 사용하기 ex) A:int=input() ....
알아둬야할 표준 라이브러리 목록.
#itertools      #반복되는 형태의 데이터를 처리하기 위한 기능들 포함 ex)순열,조합 등등..
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


########################################
https://cafe.naver.com/startdevelopercareer?iframe_url_utf8=%2FArticleRead.nhn%3FreferrerAllArticles%3Dtrue%26clubid%3D30372458%26articleid%3D6
