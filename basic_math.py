#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


#from _typeshed import NoneType


def get_greatest(number_list):
    """
    주어진 리스트에서 가장 큰 숫자를 반환함

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            greatest_number (int): parameter number_list 중 가장 큰 값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_greatest(number_list)
            99
    """
    greatest_number = 0
    
    for i in number_list:
        if i > greatest_number:
            greatest_number = i
        else:
            continue

    return greatest_number


def get_smallest(number_list):
    """
    주어진 리스트에서 제일 작은 숫자를 반환함

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            smallest_number (int): parameter number_list 중 가장 작은 값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_smallest(number_list)
            11
    """
    smallest_number = number_list[0]
    for i in number_list:
        if i < smallest_number:
            smallest_number = i
        else:
            continue
    return smallest_number


def get_mean(number_list):
    """
    주어진 리스트 숫자들의 평균을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            mean (int): parameter number_list 숫자들의 평균

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_mean(number_list)
            47
    """
    mean = 0
    sum_num = 0 
    for i in number_list:
        sum_num = sum_num + i
        #print(sum_num)

    mean = sum_num / len(number_list)

    return mean


def get_median(number_list):
    """
    주어진 리스트 숫자들의 중간값을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            median (int): parameter number_list 숫자들의 중간값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_median(number_list)
            39
            >>> number_list2 = [39, 54, 32, 11, 99, 5]
            >>> bm.get_median(number_list2)
            35.5
    """
    median = 0

    number_list.sort()
    if (len(number_list) % 2) == 0:
        median = (number_list[int(len(number_list) /2)] + number_list[int(len(number_list) /2+1)])/2
    else:
        median = number_list[int(len(number_list) /2)]

    return median

number_list = [39, 54, 32, 11, 99, 88, 123]

print(f'최댓값은 {get_greatest(number_list)}입니다.')
print(f'최솟값은 {get_smallest(number_list)}입니다.')
print(f'평균은 {get_mean(number_list):.1f}입니다.')
print(f'중앙값은 {get_median(number_list)}입니다.')