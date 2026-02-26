from random import random

# a和b只打一个球，由用户输入接住球的概率，来表示球员的能力
def playerinput():
    a_change=eval(input("请输入A球员的能力(接住球的概率,范围0-1)："))
    b_change=eval(input("请输入B球员的能力(接住球的概率,范围0-1)："))
    return a_change,b_change

def playGame(a_change,b_change):
    print(
        playOne(a_change, b_change)
    )


#胜利的条件
def gameover(A_score,B_score):
    return A_score==15 or B_score==15

#是否接到了球
def Receive(a):
    if random()>a:
        return "false"
    else:
        return "true"

#一局比赛
def playOne(a_change,b_change):
    serve='A'
    a_score=0
    b_score=0
    count=0
    while not gameover(a_score,b_score):
        #开球

        if serve=="A":
            if Receive(b_change)=='false':
                a_score+=1
                count+=1
            else:
                serve="B"
                count+=1
        elif serve =="B":
            if Receive(a_change)=='false':
                b_score+=1
                count+=1

            else:
                serve="A"
                count+=1

    return a_score,b_score,count


if __name__ == '__main__':
    a,b=playerinput()
    print(a)
    print(b)
    playGame(a,b)

