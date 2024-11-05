# Fibonacci Series
# a type series where each number is the sum of the two that precede it.
# It starts from 0 and 1 usually.
# The Fibonacci sequence is given by 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.

def fibonacci_series(length):
    x = [0, 1]

    while len(x) != length:
        x.append(x[-1] + x[-2])
    print(x)

fibonacci_series(13)