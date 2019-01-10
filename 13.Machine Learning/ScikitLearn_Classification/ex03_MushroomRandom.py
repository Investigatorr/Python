# 8000개의 버섯데이터, 22개의 특징을 학습해 독성여부 판단하기

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

# Mushroom.csv import with Pandas

df = pd.read_csv('mushroom.csv', encoding = 'utf-8 sig', header = None)
#print(df) 데이터 잘 읽었는지 확인

'''
1단계 - 레이블(클래스)과 특징량 분리 
2단계 - 특징량의 데이터들을 수치화(문자열을 유니코드로 변환) 중요!!!!
=> 1~2단계 굉장히 중요

3단계 - 훈련 데이터와 테스트 데이터 분리, train_test_split()
4단계 - 학습, fit()
5단계 - 테스트 데이터로 예측, predict()
6단계 - 결과값 test, accuracy_score()
'''
label = []
data = []

'''
데이터 프레임에는 iterrows()함수가 있는데, for문과 함께 사용시 행(row) index와 data를 한 행씩 반환
0 poison
1 null
2 normal

'''
for row_index, row in df.iterrows():  # 가로 행 단위로 읽어들임
    #print(row_index, '-', row_data) 이러면 마아아아악 뜬다
    label.append(row.iloc[0])
    #data.append(row_data.iloc[:, [1:]])
    row_data = []

    for v in row.iloc[1:]:
        row_data.append(ord(v))
    data.append(row_data)
#print(data)

data_train, data_test, label_train, label_test = train_test_split(data, label)


# 학습기 => 예측 =>  결과 test(정답률 확인)

clf = RandomForestClassifier()
clf.fit(data_train, label_train)

predict = clf.predict(data_test)
#print(predict)   ['e' 'p' 'p' ... 'p' 'e' 'p']

ac_score = metrics.accuracy_score(label_test, predict)
print(ac_score)





