import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

# 붓꽃의 CSV 데이터 읽어 들이기 
#TODO  ('iris.csv')

# 필요한 열 추출하기 
csv_data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
csv_label  #TODO 


# 학습 전용 데이터와 테스트 전용 데이터로 나누기 
train_data, test_data, train_label, test_label  #TODO

# 데이터 학습시키고 예측하기 
#TODO 
 
# 정답률 구하기 
ac_score   #TODO 
print("정답률 =", ac_score)

 
