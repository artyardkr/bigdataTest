import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # 100개의 랜덤 X값 생성
y = 4 + 3 * X + np.random.randn(100, 1)  # 선형 방정식 y = 4 + 3x + noise

# 데이터 시각화
plt.scatter(X, y, color='blue', alpha=0.5)
plt.title("Generated Data")
plt.xlabel("X")
plt.ylabel("y")
plt.show()

model = LinearRegression() # model 에 아무거나 적어도 상관없음 (asdf이런식으로써도 상관없음)
model.fit(X, y)

print("절편 (Intercept):", model.intercept_)
print("기울기 (Slope):", model.coef_)

# 3. 예측 및 결과 시각화
X_new = np.array([[0], [2]])  # X=0과 X=2일 때 예측
y_pred = model.predict(X_new)

print("예측값", y_pred)