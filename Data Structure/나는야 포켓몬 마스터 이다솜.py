#https://www.acmicpc.net/problem/1620
import sys
#from collections import deque
input = sys.stdin.readline

N,M = input().split()
pokemon_list= {}
pokemon_list2={}
for i in range(1,int(N)+1):
    name = input().rstrip()
    pokemon_list[name]=i
    pokemon_list2[i]=name
for i in range(int(M)):
    what = input().rstrip()
    if what.isalpha():  #이름을 말함
        print(pokemon_list[what])
    else:               #번호를 말함
        what=int(what)
        print(pokemon_list2[what])

#예.. 리스트로는 구현이 쉬운데 시간초과가 나옵니다.. deque가 빠르긴해도 결국 O(N) 인가봅니다.. 
#dict 은 O(1) 수준으로 key 값만 알면 가능하기때문에 dict으로 구현햇습니다 ㅎ..
