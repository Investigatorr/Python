import mglearn
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from sklearn.datasets import load_breast_cancer
import numpy as np
import pandas as pd

# 1단계 - pca적용전에 각 특성이 분산이 1이 되도록 데이터의 스케일 ㅈ ㅗ정

from sklearn.preprocessing import StandardScaler
cancer = load_breast_cancer()
scaler = StandardScaler()
scaler.fit(cancer.data)
X_Scaled = scaler.transform(cancer.data)

# 2단계 - PCA적용
from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
pca.fit(X_Scaled)

x_pca = pca.transform(X_Scaled)
print("PCA전 데이터 형태 :", X_Scaled.shape)  #(569, 30)
print("PCA전 데이터 형태 :", x_pca.shape)     #(569, 2)

# 3단계 -시각화
mglearn.discrete_scatter(x_pca[:, 0], x_pca[:, 1], cancer.target)
plt.legend(['maligant', 'benign'], loc = 'best')
plt.xlabel('1st Component')
plt.ylabel('2nd Component')
plt.show()  # 결과치를 보니 두개의 뭉치로 이루어져 있다. => 군집분석 ㄱㄱ 각 성분의 평균치 이용

# 4단계 - cancer.target 사용하지 않고 주성분 두가지로 군집화
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 2)
kmeans.fit(X_Scaled)
mglearn.discrete_scatter(x_pca[:,0], X_Scaled[:,1], kmeans.labels_, markers = '^')   # kmeans.labels_
plt.legend(['maligant', 'benign'], loc = 'best')
plt.xlabel('1st Component')
plt.ylabel('2nd Component')
plt.show()

