def function_with_uncommon_error_solution(a, b):
    if b == 0:
        return a # handle division by zero
    elif a == 0:
        return b
    else:
        return a / b

result = function_with_uncommon_error_solution(10, 0) # this now returns 10 instead of throwing an error