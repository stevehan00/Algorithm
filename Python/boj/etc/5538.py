s = list(input())

maxi = 0

for i in range(len(s)):
    if s[i] != 'J':
        continue
    j_cnt = 1
    for j in range(i+1, len(s)):
        if s[j] != 'J':
            break
        j_cnt+=1
    
    if i+3*j_cnt > len(s):
        continue

    if "".join(s[(i+j_cnt):(i+2*j_cnt)]) == 'O'*j_cnt:
        if "".join(s[(i+2*j_cnt):(i+3*j_cnt)]) == 'I'*j_cnt:
            if j_cnt > maxi:
                maxi = j_cnt


print(maxi)