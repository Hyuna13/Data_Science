#소스 from EBS 수학과 함께하는 AI기초

import pandas as pd #pandas 사용
import matplotlib.pyplot as plt #matplotlib 사용

fifa2019 = pd.read_csv('fifa2019.csv') #데이터 불러오기
print(fifa2019.shape) #shape 함수: 데이터프레임의 행,열의개수 반환
print(fifa2019.info()) #열 별로 확인

sub1 = fifa2019.loc[14]#선수 데이터 검색
print(sub1)

sub2 = fifa2019.loc[2:16]#원하는 범위 데이터
print(sub2)

sub3 = fifa2019.loc[:,['Name','Preferred Foot']]#전체선수 이름과 선호하는발
print(sub3)

sub4 = fifa2019.iloc[0:10, 1:3]#원하는 행,열 출력
print(sub4)

korea_player = fifa2019['Nationality'] == 'Korea Republic' #대한민국 선수들 출력
sub5 = fifa2019.loc[korea_player]
print(korea_player) #bool
print(sub5)

sub6 = sub5['Name'] #대한민국 선수들 이름
print(sub6)

#그래프 그리기 #matplotlib을 통해 데이터 시각화 
fifa2019['Preferred Foot'].value_counts().plot(kind = 'bar') #선호하는 발의 종류 막대그래프로 나타내기
plt.legend() #범례표시
plt.show() #그래프 출력

fifa2019['Preferred Foot'].value_counts().plot(kind = 'pie', autopct = '%1.f%%')#원그래프로 나타내기
plt.legend()
plt.show()

