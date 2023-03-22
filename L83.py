#Grace and Vinni
def count_character(x,y):
    count=0
    for ch in x:
        if ch == y:
            count=count+1
    return count
print (count_character("happy","p"))
