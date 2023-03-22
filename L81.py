#Grace and Vinni
def total_length(x):
    sum=0
    for y in x:
        sum=len(y)+sum
    return sum
total_length(['Happy','birthday'])
