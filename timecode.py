import time

def time_execution(code):
    start = time.clock()
    # eval executes what's passed to the procedure
    # e.g. time_execution('1 + 1') results in executing 1 + 1
    # and assigning result of 2 to result
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time, str(run_time * 10**6) + " us"

def spin_loop(n):
    i = 0
    while i < n:
        i += 1

