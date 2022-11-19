from collections import deque
#1과 0으로 되어있는 미로의 정보가 주어진다.0은 괴물이있어서 지나가지못하고, 출발지점과 도착지점은 항상1이다.
#(탈출불가능한 조건은없음) + 첫째줄에 N과 M이 각각주어지고 0과1로되어있는 미로의 정보가주어진다.
#이경우 최소한 움직여서 도착지점까지 간다고했을때의 움직인 횟수는?
#입력ex 5 6                 출력 10
#       101010
#       111111
#       000001
#       111111
#       111111         
def maze(x,y):
    Queue=deque()
    Queue.append((x,y))
    while Queue:
        x,y=Queue.popleft()
        for i in range(4):
            dx=x+dis_x[i]
            dy=y+dis_y[i]
            if dx<0 or dy<0 or dx>=N or dy>=M:
                continue    #미로칸수를 넘어갈경우.
            if check_list[dx][dy]==0:
                continue    #현재칸이 괴물있는칸일경우
            if check_list[dx][dy]==1:           #현재칸이 처음방문하는 경우에만.
                check_list[dx][dy]=check_list[x][y]+1
                Queue.append((dx,dy))
    return check_list[N-1][M-1]
        

N,M=map(int,input().split())
check_list=[]
dis_x=[-1,1,0,0]
dis_y=[0,0,-1,1]
for i in range(N):
    check_list.append(list(map(int,input())))

print(maze(0,0))