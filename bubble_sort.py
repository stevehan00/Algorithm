def bubble_sort(num_list):
    for i in range(len(num_list)-1, 0, -1):
        for j in range(0, i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return


if __name__ == '__main__':
    lst = [2, 3, 5, 4, 1]
    bubble_sort(lst)

    for i in lst:
        print(i, end=' ')
