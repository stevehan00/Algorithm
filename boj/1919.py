from collections import Counter

a = input()
b = input()
s1 = Counter(list(a))
s2 = Counter(list(b))

cnt = 0
for c in s1:
    if c in s2:
        if s1[c] == s2[c]:
            cnt += s2[c]
        else:
            cnt += min(s1[c], s2[c])

print(len(a)+len(b)-cnt*2)