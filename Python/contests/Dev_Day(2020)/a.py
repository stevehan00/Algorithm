def solution(src):
    answer = []

    answer.append(src[0])

    cnt = 1
    for c  range(1, len(src)):
        if src[c-1] == src[c]:
            cnt += 1
        else:
            print(cnt)
            answer.append(chr(64+cnt))
            cnt = 1

    if cnt != 1:
        answer.append(chr(64+cnt))

    return ''.join(answer)