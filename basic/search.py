def linear_search(lst, num):
    for i in range(len(lst)):
        if lst[i]==num:
            return i

def binary_search(lst, num):
    lst.sort()
    start = 0
    end = len(lst)-1

    while start <= end:
        mid = (start+end)//2

        if lst[mid] == num:
            return mid
        elif lst[mid] < num:
            start = mid + 1
        else:
            end = mid-1


def binary_search_recursion(num, start, end, lst):
    if start > end:
        return None
    mid = (start+end)//2

    if lst[mid]==num:
        return mid
    elif lst[mid] > num:
        end = mid-1
    else:
        start = mid+1

    return binary_search_recursion(num, start, end, lst)


if __name__=='__main__':
    num_list=[5,4,3,2,1]

    print(linear_search(num_list, 3))

    print(binary_search(num_list, 3))

    print(binary_search_recursion(3, 0, len(num_list)-1, num_list))