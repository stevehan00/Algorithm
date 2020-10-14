def hanoi(num, froms, by, to):

    if num == 1:
        print(froms,to)
        return
    hanoi(num-1, froms, to, by)
    print(froms,to)
    hanoi(num-1, by, froms, to)

if __name__=='__main__':
    disk = int(input())
    print(2**disk-1)
    hanoi(disk, '1', '2', '3')