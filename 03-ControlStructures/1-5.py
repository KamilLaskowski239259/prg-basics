# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
total_tasks = 20
tasks_ok = int(input("Enter amount of tasks done correctly: "))
test_passed = False

if tasks_ok + total_tasks >= 30 :
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')