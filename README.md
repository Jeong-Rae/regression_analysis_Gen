에러측정 함수 설명

유전자 생성함수 설명
- (w:f,b:i)인 유전체 4개 생성
'''
for i in range(4): #1세대 생성
        num1=random.uniform(0,slope_max) #자료 기울기 최소~최대
        num2=random.randint(0,y_max) #자료 크기 최소~최대
        gen[i]=(num1,num2)
'''

- 각 유전체별 적합도측정(에러역수이용)
- 가중치 선택
- 100% 교차
- 확률에 따른 변이 w,b 개별적인 확률
- 반복

데이터 셋 설명
- 2xerr(-1~1:f)x + 0 + err(-10~10:i}, size=100 으로 생성된 데이터

회귀유사도 비교
- 데이터셋과 2x의 오차값, 기존오차값/0.95= 요구 요차값 으로 테스트
- 결과 그래프 비교

돌연변이에 따른 세대수 비교
- 0.005 0.01 0.05 0.1 비교 돌연변이 확률 : K/시행회수 즉 반비례관계가 성립
- ResultDataAboutMu 에서 확인 가능

평균 세대수 비교
- 돌연변이 0.01 고정, 500번 시행
- 히스토그램
- 추정 평균

최적화 과정 확인
- 요구오차=기존오차/0.99
- 실행결과 유전체별 오류값 변화 데이터
- ResultDataAboutErr 에서 데이터 확인 가능
- 산점도 

