# 정답률 구하기, 정답률로 가설의 신뢰성 확인
# 1차 : 함수 기능
# 2차 : 함수 검증
# 3차 : test데이터 직접 구성해서 모델 검증을 데이터로만 해보기


from sklearn import svm
# XOR의 계산 결과 데이터 --- (※1)
xor_data = [
    #P, Q, result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]



# 학습을 위해 데이터와 레이블 분리하기 --- (※2)
data = []
label = []
for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    
    #TODO
    # data 변수에 학습용 데이터 저장
    data.append([p,q])
#print(data) 이거 코드 활성화되면 반복문이 끝난거나 다름 없음
# [[0, 0], [0, 1], [1, 0], [1, 1]]

    #TODO
    # label 변수에 레이블 데이터 저장
    label.append(r)
print(label)
    
# 데이터 학습시키기 --- (※3)
#TODO
clf = svm.SVC()
clf.fit(data, label)
    
    
# 데이터 예측하기 --- (※4)
#TODO
pre = clf.predict(data)
print("예측결과 : ", pre)   # 예측결과 :  [0 1 1 0]
 





    
# 결과 확인하기 --- (※5)
ok = 0; total = 0
for idx, answer in enumerate(label):
    p = pre[idx]
    if p == answer :
        ok += 1
        total += 1
    
print("정답률:", ok, "/", total, "=", ok/total     ) #TODO 
