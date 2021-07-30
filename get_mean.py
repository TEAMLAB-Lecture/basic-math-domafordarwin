# 제작일: 2021년 7월 29일 08시 30분

# 과제 - 주어진 리스트에서 가장 작은 숫자를 반환함

# 의사코드 작성하기
# 1. 리스트 생성하기
# 2. 리스트에 있는 숫자들의 크기 비교하기
## 리스트 불러오기 for 문 활용
# 2.1. 리스트에서 첫 번째 숫자와 두 번째 숫자를 불러오기
# 2.2. 숫자를 더해서 값 저장하기
# 2.3. 다음 차례의 숫자를 불러와서 더하기
# 2.4. 최종 숫자를 리스트 갯수로 나누기
# 2.4. 최종적으로 저장된 값  출력하기


# 필요한 라이브러리 불러오기
import random

# 리스트 생성하기
num_list = []

# 리스트에 무작위 값 배정하기
for i in range(5):
    num_list.append(random.randrange(1, 100))
    print(num_list)

    

# 평균 구하기
sum_num = 0

for i in num_list:
    sum_num = sum_num + i
    print(sum_num)

mean = sum_num / len(num_list)
# 최종값 출력하기
print(mean)
