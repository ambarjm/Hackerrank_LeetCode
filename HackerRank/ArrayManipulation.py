def arrayManipulation(n, queries):
    seq=[0] * (n+1)
    for x , y , z in queries:
        x=x-1
        seq[x]+=z
        seq[y]-=z
    max_value = 0
    running_count=0
    for i in seq:
        running_count=running_count+i
        if running_count> max_value:
            max_value=running_count
    return max_value
        
    return max(seq)
