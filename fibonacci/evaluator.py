# Test case evaluator, test cases will be in a JSON file. We'll edit the
# function contents for each person.
import timeit
import json
test_cases = json.loads(open("test_cases.json","r").read())
def fib(x):
    # Replace this function with student-submitted code
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
failed = False
total_time = 0
for case in test_cases:
    output = fib(case['input'])
    if case['output']==output:
        time_taken = timeit.timeit('fib(' + str(case['input']) +')','from __main__ import fib',number=100)
        total_time+=time_taken
        print("Passed test case " + case['name'] + " in " + str(time_taken) + " seconds")
    else:
        failed=True
        print("Failed test case " + case['name'] + " with output " + output)
if failed:
    print("Code failed.")
else:
    print("Code succeeded with a total time of " + str(total_time)) 
