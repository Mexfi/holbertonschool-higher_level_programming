#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end='')  # Çap edilən elementlər bir yerdə göstərilir
            count += 1
    except IndexError:
        pass  # Siyahı bitərsə, sadəcə davam et

    print()  # Yeni sətirə keçmək üçün bu buradadır
    return count
