"""B 2004 조합 0의 개수(Number of Zero in Combination)
Problem:
    Combination(n, m)의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오.

Input:
    첫째 줄에 정수 n, m 이 들어온다.(0 <= m <= n <= 2,000,000,000, n != 0)

Output:
    첫째 줄에 Combination(n, m)의 끝자리 0의 개수를 출력한다.
"""

def solution():
    """Combination(n, m)의 2의 개수와 5의 개수 중 적은 값을 구해 출력한다.
    Extra explanation:
        Combination(n, m) = n!/m!(n-m)! 값의 끝자리 0의 개수는 combination 값의 2의 개수와 5의 개수 중 더 적은 개수를 구하면 된다.
        따라서, 각 factorial 값의 2의 개수와 5의 개수를 구해야 한다.
        Factorial 값의 2의 개수와 5의 개수는 count() method를 이용해 구한다.
    
    Variables:
        n, m : 주어진 정수 n, m
        number_of_two : Combination(n, m)의 2의 개수
        number_of_five : Combination(n, m)의 5의 개수
    
    Example:
        >>> 25 12   : input n, m
        >>> 2       : output result
    """
    n, m = map(int, input().split())
    number_of_two = count(n, 2) - count(m, 2) - count(n-m, 2)
    number_of_five = count(n, 5) - count(m, 5) - count(n-m, 5)
    print(min(number_of_two, number_of_five))

def count(n, k):
    """주어진 정수 n!에서 k의 개수를 구해 반환한다.

    Variables:
        result : n!에서 k의 개수
    
    Example:
        >>> count(25, 2)    : returns result = 22
    """
    result = 0
    while n:
        n //= k
        result += n
    return result

solution()