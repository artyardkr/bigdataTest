import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 한글 폰트 설정 (macOS)
plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

# 샘플 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 1. 기본 선 그래프
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')
plt.title('기본 선 그래프')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

# 2. 산점도
plt.subplot(2, 2, 2)
x_scatter = np.random.randn(50)
y_scatter = np.random.randn(50)
plt.scatter(x_scatter, y_scatter, alpha=0.6, c='red')
plt.title('산점도')
plt.xlabel('x')
plt.ylabel('y')

# 3. 히스토그램
plt.subplot(2, 2, 3)
data = np.random.randn(1000)
plt.hist(data, bins=30, alpha=0.7, color='green')
plt.title('히스토그램')
plt.xlabel('값')
plt.ylabel('빈도')

# 4. 막대 그래프
plt.subplot(2, 2, 4)
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]
plt.bar(categories, values, color='orange')
plt.title('막대 그래프')
plt.xlabel('카테고리')
plt.ylabel('값')

plt.tight_layout()
plt.show()

print("matplotlib 그래프가 표시되었습니다!")
