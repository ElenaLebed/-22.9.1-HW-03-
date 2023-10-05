def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return mid


def sort_list(lst):
    return sorted(lst)


numbers = input("Введите последовательность чисел через пробел: ")
numbers_list = numbers.split()

try:
    numbers_list = [int(num) for num in numbers_list]
except ValueError:
    print("Ошибка! Некорректный ввод чисел.")
    exit()

numbers_list = sort_list(numbers_list)

target = input("Введите любое число: ")

try:
    target = int(target)
except ValueError:
    print("Ошибка! Некорректный ввод числа.")
    exit()

position = binary_search(numbers_list, target)

if position == len(numbers_list) - 1:
    print("Введенное число больше всех чисел в последовательности.")
else:
    print("Позиция введенного числа:", position)