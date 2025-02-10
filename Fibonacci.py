import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
test_cases = list(map(int, input_data[1:N+1]))

memo = {}

for x in test_cases:
    n = x
    calls_count = 0

    if n in memo:
        result, calls = memo[n]
    else:
        if n == 0:
            result, calls = 0, 0
        elif n == 1:
            result, calls = 1, 0
        else:
            fib_values = {0: (0, 0), 1: (1, 0)}
            for i in range(2, n + 1):
                fib1, calls1 = fib_values[i - 1]
                fib2, calls2 = fib_values[i - 2]
                result = fib1 + fib2
                calls = calls1 + calls2 + 2
                fib_values[i] = (result, calls)
            memo[n] = (result, calls)
    
    print(f"fib({x}) = {calls} calls = {result}")
