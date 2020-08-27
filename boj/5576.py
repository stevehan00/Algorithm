w = sorted([int(input()) for _ in range(10)], reverse = True)[:3]
k = sorted([int(input()) for _ in range(10)], reverse = True)[:3]
print(sum(w), sum(k))