import matplotlib.pyplot as plt
import numpy
import pandas as pd
import math
import random



def Read(): # 자료 불러오기
    
    raw_data = pd.read_csv('randomdataset.csv', encoding = 'utf-8')
    
    raw_data['x'].astype(int), raw_data['y'].astype(float)
    x_data,y_data =raw_data['x'].values.tolist(), raw_data['y'].values.tolist()
    
    return x_data, y_data

def L_funtion(w,b,data): #일차함수 wx+b, 출력: 함수값
    return w*data+b

def Plot(w,b): # 결과 그래프 출력
    
    t_data=[L_funtion(w,b,i) for i in x_data]
    plt.scatter(x_data, y_data, color='#724199')

    plt.plot([0,100],[0,200], color='#012030')
    plt.text(5,250,'raw function', color='#012030')
    plt.text(5,235,': y= 2x', color='#012030')
    
    plt.plot(x_data, t_data, color='#13678A')
    plt.text(5,200,'regressed function', color='#13678A')
    plt.text(5,185, ': '+str(w)+'x'+'+'+str(b), color='#13678A')
    
    plt.show()
    
def ErrorVerification(w,b): #출력: 편차제곱합/표본크기
    total_error=0
    for i in range(size):
        error= L_funtion(w,b,x_data[i]) - y_data[i]
        total_error= total_error+ error*error
        
    return total_error/size   
    return math.log(total_error)

def Generate(N,M,C): # N세대 생성, 변이확률 1/m, 적합도
    
    gen, newgen, fit =[[0,0],[0,0],[0,0],[0,0]], [[0,0],[0,0],[0,0],[0,0]], []
    mutimes=0
    slope_max = 3
    y_max = 264/2
    
    for i in range(4): #1세대 생성
        
        
        num1=random.uniform(0,slope_max) #자료 기울기 최소~최대
        num2=random.randint(0,y_max) #자료 크기 최소~최대
        gen[i]=(num1,num2)
        
    #print('1세대', gen) 
    j=0
    while True: #for j in range(N-1): # N 세대 생성
        for i in range(4): #적합도 계산
            fit.append(100/ErrorVerification(gen[i][0],gen[i][1]))
            
        for i in range(4):  #교차선택으로 다음 세대 생성
            temp=random.choices(gen,fit,k=2) #가중치 선택
            newgen[i][0],newgen[i][1]=temp[0][0],temp[1][1]
            
            #변이
            if random.randint(1,M)%M==0:
                mu_num1=random.uniform(0,slope_max)
                newgen[i][0]=mu_num1
                mutimes+=1
            if random.randint(1,M)%M==0:
                mu_num2=random.randint(0,y_max)
                newgen[i][1]=mu_num2
                mutimes+=1
                
           
        print(j+2,'세대', newgen)
        
        gen = newgen
        newgen, fit =[[0,0],[0,0],[0,0],[0,0]], []
        
        
        if ErrorVerification(gen[0][0],gen[0][1]) <C :
            #print(ErrorVerification(gen[0][0],gen[0][1]))
            return gen[0][0], gen[0][1], j+2, ErrorVerification(gen[0][0],gen[0][1]), mutimes
        elif ErrorVerification(gen[1][0],gen[1][1]) <C :
            #print(ErrorVerification(gen[1][0],gen[1][1]))
            return gen[1][0], gen[1][1], j+2, ErrorVerification(gen[1][0],gen[1][1]), mutimes
        elif ErrorVerification(gen[2][0],gen[2][1]) <C :
            #print(ErrorVerification(gen[2][0],gen[2][1]))
            return gen[2][0], gen[2][1], j+2, ErrorVerification(gen[2][0],gen[2][1]), mutimes
        elif ErrorVerification(gen[3][0],gen[3][1]) <C :
            #print(ErrorVerification(gen[3][0],gen[3][1]))
            return gen[3][0], gen[3][1], j+2, ErrorVerification(gen[3][0],gen[3][1]), mutimes
        j=j+1
        

### MAIN ###
x_data, y_data = Read()
size=len(x_data)
result_data = [] # w값, b값, 세대, 오류값, 변이횟수
C=ErrorVerification(2,0)/0.95


for i in range(10): #변이 1%
    result_data.append(Generate(1000000,100,C))
    
    print(i+1,'회 종료')

df=pd.DataFrame(result_data, columns=['w','b','Generation','Error','Mutation']) #결과저장
print(df)
df.to_csv("ResultData200Try.csv", index = False)
