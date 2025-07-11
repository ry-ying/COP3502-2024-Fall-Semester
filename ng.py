def is_palindrome(n):
    return str(n) == str(n)[::-1]

def count_palindromic_factors(A):
    count = 0
    for i in range(1, int(A**0.5) + 1):
        if A % i == 0:
            if is_palindrome(i):
                count += 1
            if i != A // i and is_palindrome(A // i):
                count += 1
    return count

# Read input
T = int(input('hi'))
for case_num in range(1, T + 1):
    A = int(input())
    result = count_palindromic_factors(A)
    print(f"Case #{case_num}: {result}")

