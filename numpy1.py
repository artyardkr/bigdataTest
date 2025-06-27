import numpy as np 

a = np.array([1,2,3,4,5,6])
print(a)
b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b.shape)


#배열 조작
#크기 변경 (reshape)
array = np.array([1, 2, 3, 4, 5, 6])
reshaped_array = array.reshape((2, 3))
print(reshaped_array)

#평탄화(한줄로 다시바꾸기)(이미지를 바꿨을떄 )



#배열연산
#기본연산

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)  # [5 7 9]
print(x - y)  # [-3 -3 -3]
print(x * y)  # [4 10 18]
print(x / y)  # [0.25 0.4  0.5 ]

#통계함수
print(np.sum(x))  # 6  총합
print(np.mean(x))  # 2.0 평균
print(np.std(x))  # 0.816496580927726   #표준편차
print(np.min(x))  # 1  최소값
print(np.max(x))  # 3 최대값


#인덱싱

arr = np.array([1, 2, 3, 4, 5])
print(arr[0])  # 1
print(arr[-1])  # 5
print(arr[1:3])# 2,3
#2차원 배열 인덱싱 및 슬라이싱
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])