"""
Sample: Human-written code
MindPrint should detect strong human trace
"""

def fibonacci_human(n):
    # I always forget base case, adding comment to remember
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # My old college trick - iterative is faster
    a, b = 0, 1
    for i in range(2, n+1):
        # temp variable because I like clear code
        temp = a + b
        a = b
        b = temp
    return b

# Testing with my lucky number
print(fibonacci_human(7))  # should be 13
