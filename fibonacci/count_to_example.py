# Counting example to show to new programmers so they can use it as a base
def count_to(x):
    string = "1"
    for i in range(2, x+1):
        string += ", " + str(i)
    return string
print(count_to(10))
