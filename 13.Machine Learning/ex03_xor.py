'''
 API에서 제공하는 정답률 구하는 함수 사용해보기
 metrics

'''

import pandas as pd
from sklearn import svm, metrics
# XOR 연산
xor_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
# 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류하기 --- (※1)
xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.iloc[:, [0,1]]    # 데이터
xor_label = xor_df.iloc[:, 2]    # 레이블

# 데이터 학습과 예측하기 --- (※2)
# TODO 
clf = svm.SVC()
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)
print("예측결과 : ", pre)

# 정답률 구하기 --- (※3)
# TODO

ac_score = metric.accuracy_score(xor_label, pre)
print("정답률 =", ac_score)
