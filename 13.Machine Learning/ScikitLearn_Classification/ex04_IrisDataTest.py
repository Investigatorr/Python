'''
마무리 자가진단 프로그래밍

1. 데이터셋 : 사이킷런 Iris 데이터셋

2. feature와 label(클래스) 존재

3. 학습, 예측, 정답률 도출해내기
'''

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import datasets

iris = datasets.load_iris()
print(iris)