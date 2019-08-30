def selection_sort(array):
    for i in range(len(array)-1): #i => 최소 값을 찾아서 끼워넣을 인덱스
        min_index=i
        for j in range(i+1, len(array)): #최소 값 찾기
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


if __name__=='__main__':
    num_list=[3,2,4,1,5]
    selection_sort(num_list)

    for i in num_list:
        print(i, end=' ')