from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    music = defaultdict(list)
    play_num = defaultdict(int)
    
    for i in range(len(plays)):
        g = genres[i]
        p = plays[i]
        
        play_num[g] += p
        music[g].append([i,p])
        
    # genre order
    orders = sorted(play_num.items(), key=lambda x:-x[1])

    for genre in orders:
        lst = music[genre[0]]
        if len(lst)==1:
            answer.append(lst[0][0])
        else:
            lst = sorted(lst, key=lambda x:(-x[1],x[0]))
            answer.append(lst[0][0])
            answer.append(lst[1][0])
    
    
    return answer