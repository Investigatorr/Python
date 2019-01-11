# 선형 회귀 시본예제
# 공부 시간으로 점수 예측해보기

from sklearn.linear_model import LinearRegression

# 공부시간
x = [[10], [5], [9],[1]]

# 점수
y = [[100], [50], [90], [70]]

model = LinearRegression()
model = model.fit(x, y)

result = model.predict([[7]])    # 2차원으로 넣어야 하나??
print(result)


# 공부시간
x2 = [[10, 3], [5, 2], [9, 3],[7, 3]]

# 점수
y2= [[100], [50], [90], [70]]

model2 = LinearRegression()
model2 = model.fit(x, y)

result2 = model.predict([[9,2]])    # 2차원으로 넣어야 하나??
print(result2)






