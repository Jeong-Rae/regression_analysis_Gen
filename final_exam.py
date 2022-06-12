import csv
import matplotlib.pyplot as plt
import numpy as np
import math
import random


data_x, data_y=[],[]

with open('student_info.csv', 'r', encoding='utf-8') as csv_file: #데이터셋 불러오기
    csv_data=csv.reader(csv_file)
    for data in csv_data:
        data_x.append(int(data[0]))
        data_y.append(int(data[1]))

def plot(w,b): # 그래프
    data_t=[L_funtion(w,b,i) for i in data_x]
    plt.scatter(data_x, data_y)
    plt.plot(data_x, data_t)
    plt.show()
      
def L_funtion(w,b,data): #일차함수 wx+b, 출력: 함수값
    return w*data+b

def ErrorVerification(w,b): #출력: ln(편차제곱합)
    total_error=0
    for i in range(90):
        error= L_funtion(w,b,data_x[i]) - data_y[i]
        total_error= total_error+ error*error
        
    return math.log(total_error)

def generation(N): # N+1세대 생성, 출력: N+1 세대
    
    Fit=[]
    Gen=[]
    newGen=[[0,0],[0,0],[0,0],[0,0]]   
    p=40 #변이상수
    
    for i in range(4):
        num1=random.uniform(0,5)
        num2=random.randrange(0,200)
        list=[num1,num2]
        Gen.append(list)
    
    for j in range(N): # N+1 세대 생성
        for i in range(4): #적합도 계산
            Fit.append(100/ErrorVerification(Gen[i][0],Gen[i][1]))
            
        for i in range(4):  #교차선택으로 2세대 생성
            FitGen=random.choices(Gen,Fit,k=2) #가중치 선택
            newGen[i][0],newGen[i][1]=FitGen[0][0],FitGen[1][1] #뉴젠에 초기화
            
            a,b=random.randint(1,p),random.randint(1,p) #변이
            if a%p==0:
                print(j+1,'세대에서 a 변이')
                mu_num1=random.uniform(0,5)
                newGen[i][0]=mu_num1
            if b%p==0:
                print(j+1,'세대에서 b 변이')
                mu_num2=random.randrange(0,200)
                newGen[i][1]=mu_num2

            
        print(j+1,'세대', Gen)    
        print(j+2,'세대', newGen)
        print()

        Gen=newGen
        newGen=[[0,0],[0,0],[0,0],[0,0]]
        Fit=[]
        
    
    return Gen



last_G=generation(19)
for i in range(4):
    print(ErrorVerification(last_G[i][0],last_G[i][1]))


plot(last_G[0][0],last_G[0][1])
