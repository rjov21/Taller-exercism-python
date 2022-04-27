def latest(scores):
    x = scores[len(scores)-1]
    return x
        


def personal_best(scores):
    best = scores[0]
    for x in scores:
        if x > best:
            best = x
    return best


def personal_top_three(scores):
    x = []
    scores.sort(reverse=True)
    size = len(scores)
    if size <= 3:
        for i in scores:
            x.append(i)
    else:
        for i in range(0,3):
            x.append(scores[i])
    return x    
