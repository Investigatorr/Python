#TODO 
#xar 데이터값 예측하느 ㄴ프로그램
# 테스트 데이터 + 결과치도 제공
# 식별 경계를 기준으로 데이터 예측

#library
from sklearn import svm


# Support Vectior Classification 약어
# svm을 기준으로 분류하는 함수
# 데이터 +답 => 예측하고 검증해서   적합한 모델 검증 =>
clf = svm.SVC()

# 학습함수
cfl.fit(
    [[0,1], 
    [1,0], 
    [0,1], 
    [1,1], 
    [0,1,1]
], [0,1,1,0])

# 예측하는 함수
results = clf.predict([0,0], [1,0])
print(results)