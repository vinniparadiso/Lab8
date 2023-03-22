#Grace and Vinni
def until_dot(x):
    index=0
    while index<len(x) and x[index] != ".":
        index+=1
    print(x[:index])

x="This is a sentence. This is another."
print(until_dot(x))
