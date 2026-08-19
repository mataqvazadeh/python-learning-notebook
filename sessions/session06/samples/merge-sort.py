import random

def merge_sort(lst: list[int]) -> list[int]:
    if len(lst) == 2:
        if lst[0] > lst[1]:
            return [lst[1], lst[0]]
        else:
            return [lst[0], lst[1]]
    elif len(lst) == 1:
        return lst
    
    mid = len(lst) // 2
    left_lst = lst[:mid]
    right_lst = lst[mid:]
    sorted_left_lst = merge_sort(left_lst)
    sorted_right_lst = merge_sort(right_lst)

    result = merge(sorted_left_lst, sorted_right_lst)
    return result

def merge(l_list, r_list):
    i, j = 0, 0
    result = []
    while i < len(l_list) and j < len(r_list):
        if l_list[i] < r_list[j]:
            result.append(l_list[i])
            i += 1
        else:
            result.append(r_list[j])
            j += 1

    if i < len(l_list):
        result.extend(l_list[i:])
    
    if j < len(r_list):
        result.extend(r_list[j:])

    return result

numbers = list(range(-10, 10))
random.shuffle(numbers)
numbers = numbers[::3]
print(numbers)
sorted_numbers = merge_sort(numbers)
print('-' * 50)
print(sorted_numbers)