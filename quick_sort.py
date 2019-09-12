def quick_sort(array):
    if len(array) > 1:
        pivot = array[-1]
        left, mid, right = [], [], []

        for i in range(len(array)-1):
            if array[i] < pivot:
                left.append(array[i])
            elif array[i] > pivot:
                right.append(array[i])
            else:
                mid.append(array[i])
        mid.append(pivot)
        return quick_sort(left) + mid + quick_sort(right)
    else:
        return array


if __name__ == '__main__':
    arr = [3, 5, 1, 2, 9, 6, 4, 7, 5]
    print(quick_sort(arr))
