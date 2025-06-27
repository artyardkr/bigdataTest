import pandas as pd

# JSON 파일 경로 설정
path = 'employee_data.json'

# JSON 파일 읽기
df = pd.read_json(path)
#강사님의 팁(구분법)
# print('========head=======')

# # 데이터 확인
# print("데이터 형태:", df.shape)
# print("\n처음 5행:")
# print(df.head())

# print("\n데이터 정보:")
# print(df.info())

# print("\n기본 통계:")
# print(df.describe())

sorted_df = df.sort_values(by='나이')
print(sorted_df.head())

grouped_df = df.groupby('부서')['나이'].mean()
print(grouped_df)

#결측치 잘못된 데이터 
print(df.isnull().sum())

missing_dept = df[df['부서'].isnull()]
print(missing_dept)


