def sum_of_multiples(limit, multiples):
    sum = 0
    a = []
    for x in range(1,limit):
        for j in multiples:
            if j != 0:
                if(x % j == 0):
                    a.append(x)
    b = set(a)
    for c in b:
        sum = sum + c
    return sum
    