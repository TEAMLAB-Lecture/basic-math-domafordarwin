# 제작일: 2021년 7월 29일 08시 30분

# 과제 - 주어진 리스트에서 가장 큰 숫자를 반환함

# 의사코드 작성하기
# 1. 리스트 생성하기
# 2. 리스트에 있는 숫자들의 크기 비교하기
## 리스트 불러오기 for 문 활용
# 2.1. 리스트에서 첫 번째 숫자와 두 번째 숫자를 불러오기
# 2.2. 숫자를 비교해서 큰 값을 저장하기
# 2.3. 다음 차례의 숫자를 불러와서 비교하기
# 2.4. 최종적으로 저장된 값 출력하기


# 필요한 라이브러리 불러오기
import random

# 리스트 생성하기
num_list = []

# 리스트에 무작위 값 배정하기
for i in range(5):
    num_list.append(random.randrange(1, 100))
    print(num_list)

    

# 값 비교하기
compare_num = 0

for i in num_list:
    if i > compare_num:
        compare_num = i
    else:
        continue

# 최종값 출력하기
print(compare_num)