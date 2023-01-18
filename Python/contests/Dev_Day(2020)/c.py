from collections import Counter

def solution(s):
    answer = 0

    cnt = Counter(s)
    print(cnt)
    answer += cnt[4]


    if cnt[2] > 1:
        answer += cnt[2]//2
        cnt[2] = cnt[2]%2 

    if cnt[3] == cnt[1]:
        answer += cnt[3]
        cnt[3] = 0
        cnt[1] = 0
        answer += cnt[2]
        return answer

    elif cnt[3] > cnt[1]:
        answer += cnt[3]
        cnt[3] = 0
        cnt[1] = 0
        answer += cnt[2]
    else:
        answer += cnt[3]
        cnt[1] = cnt[1] - cnt[3]

        if cnt[2] == 1:
            if cnt[1] > 1:
                answer += 1
                cnt[2] = 0
                cnt[1] -= 2

            else:

                answer += 1
                cnt[1] = 0
                cnt[2] = 0

        answer += cnt[1]//4
        if cnt[1] % 4 != 0:
            answer += 1



    return answer