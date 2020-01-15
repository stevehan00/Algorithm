'''
규칙
1. 원반은 위에서부터 꺼낼 수 있다
2. 한번에 하나씩 이동가능
3. 작은 원반이 위쪽에 있어야 한다
'''

'''
제일 큰 원반을 제외한 나머지 모든 기둥을 보조기둥으로 옮겨야한다.
원반이 1개일 때는 아무 노룍x ->  원래 원반 개수에서 -1한 만큼 갯수로 풀이 진행
'''

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