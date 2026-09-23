
#

# Series - 1차원 데이터 구조 : 리스트와 유사하나 각 데이터에 라벨(인덱스)이 붇음
import pandas as pd
s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)

# DataFrame - 2차원 데이터 구조 : 여러 개의 Series가 모여 이루어짐. 행과 열로 구성됨
data = {
    '이름': ['민지', '하니', '아니엘'],
    '수학': [95, 85, 75],
    '영어': [90, 85, 94]
}

df = pd.DataFrame(data)
print(df)

# 특정 행 및 열 추출
print(df['수학'])         # 열 추출
print(df.loc[0])         # 행 추출
print(df.loc[1, '영어'])  # 특정 행의 열 추출

# 새로운 열 및 행 추가
df['과학'] = [93, 89, 87] # 새 열 추가
df.loc[3] = ['혜인', 92, 89, 77]
print(df)

# 기본연산
print(df['수학'].sum())
print(df['수학'].mean())
print(df['수학'].max())
print(df['수학'].min())

# 열추가
df['반'] = [1, 1, 2, 2]
print(df)

print(df.groupby('반')['수학'].mean())