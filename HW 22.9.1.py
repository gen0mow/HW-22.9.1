def sort_list(lst):
    return sorted(lst)

def binary_search(sorted_lst, num):
    low = 0
    high = len(sorted_lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_lst[mid] < num:
            low = mid + 1
        else:
            high = mid - 1
    return low

input_seq = input("Введите последовательность чисел через пробел: ")
num = int(input("Введите любое число: "))
numbers = list(map(int, input_seq.split()))
sorted_numbers = sort_list(numbers)
position = binary_search(sorted_numbers, num)

print(f"Номер позиции элемента, который меньше {num}, а следующий за ним больше или равен этому числу: {position}")