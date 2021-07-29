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

list_len = random.randrange(1, 10)

# 리스트에 무작위 값 배정하기
for i in range(list_len):
    num_list.append(random.randrange(1, 100))
    print(num_list)

    

# 값 소팅하기
num_list.sort()

print(num_list)

if (list_len % 2) == 0:
    print(f'리스트의 갯수 {list_len}로 짝수이므로')
    median_num = (num_list[int(len(num_list)/2)] + num_list[int(len(num_list)/2+1)])/2
else:
    print(f'리스트의 갯수 {list_len}로 홀수이므로')
    median_num = num_list[int(len(num_list)/2)]
print(f'중앙값은 {median_num}입니다.')


