def insertion_sort(array):
    for i in range(1, len(array)):
        k = array[i]

        j = i-1
        while j>=0 and array[j] > k:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = k

if __name__=='__main__':
    num_list=[5,4,3,2,1]
    insertion_sort(num_list)

    for i in num_list:
        print(i, end=' ')