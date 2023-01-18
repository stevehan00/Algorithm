def hannum(n):
    start = 0
    result = 0

    while start < n:
        start += 1

        if len(str(start)) <= 2:
            result += 1

        else:
            lst = [int(j) for j in str(start)]
            pre = lst[1]-lst[0]
            temp = lst[2]-lst[1]
            if pre == temp:
                result += 1

    return result


if __name__=='__main__':
    print(hannum(int(input())))