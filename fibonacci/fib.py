number = int(input("Enter length:\n"))
def fib(x):
    # We're starting with a 1 already there to make formatting easier. Therefore, if we're asked for 0 digits, we need to make an exception
    if x == 0:
        return ""
    string = "1"
    num = 1
    old_num = 1
    # Starting at 1 since there's already a 1 in there.
    for _ in range(1,x):
        string += ", " + str(num)
        # Sets the current number to be itself plus the previous, and then sets the new previous
        old_num,num = num,old_num+num
    return string
print(fib(number))
        
