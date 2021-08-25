import pandas as pd #pandas 
import matplotlib.pyplot as plt #matplotlib 
import numpy as np #numpy 

#데이터 분석상 주제를 변경하였다.
#주제: 미국총기난사 데이터 from https://www.kaggle.com/zusmani/us-mass-shootings-last-50-years

#미국총기난사1 2016~2021
shootings = pd.read_csv('shootings.csv') #pandas 사용
print(shootings.shape)  
print(shootings.info()) 

data1 = shootings.loc[2]
print(data1)

data2 = shootings.loc[1:20]
print(data2)

data3 = shootings.loc[:,['State','# Killed']] #주, 사망자 수 
print(data3)

data4 = shootings.iloc[0:10, 1:2]
print(data4)

state = shootings['State'] == 'California' #캘리포니아 총기난사 출력 
data5 = shootings.loc[state]
print(state)
print(data5)

data6 = data5['# Killed'] #캘리포니아 내 총기난사 사망자 수 
print(data6)

shootings['State'].value_counts().plot(kind = 'bar') #전체 주,사건 수 막대그래프로 나타내기
plt.legend()
plt.show()

#추가:3개 주,사건 수 막대그래프 나타내기
print(shootings['State'].value_counts())
x = np.arange(3) #numpy사용 
state = ['Illinois', 'California', 'New York']
values = [214, 189, 83]
plt.bar(x, values, width=0.5, align='center', color="skyblue",
        edgecolor="orange", linewidth=2, tick_label=state) #추가:막대너비,위치,색,두께설정 
plt.xticks(x, state)
plt.show()



#미국 총기난사2 1966~2017
shootings2 = pd.read_csv('shootings2.csv')

#추가:원 그래프로 나타내기
shootings2['Gender'].value_counts().plot(kind = 'pie', autopct = '%.1f%%')
plt.legend()
plt.show()

print(shootings2['Gender'].value_counts()) # 각 성별에 따른 가해자 수

#F/M는 각 성별에 모두 더함

gender = ['Female','Male','Unknown']
values = [26, 313, 5]
explode = [0.2,0,0.2]
colors = ['blue','red', 'green']
plt.pie(values, labels=gender, autopct='%1.f%%', explode=explode, colors=colors) #추가:색상,확대,비율추가 
plt.legend(gender)
plt.pie(values)
plt.show()


