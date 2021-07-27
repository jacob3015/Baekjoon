"""B 1978 소수 찾기(Find Prime Number)
Problem:
    주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

Input:
    첫 줄에 수의 개수 N이 주어진다. N은 100 이하이다.
    다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

Output:
    주어진 수들 중 소수의 개수를 출력한다.
"""
import math

def solution():
    """주어진 N개의 수 중 소수의 개수를 구해 출력한다.
    Extra explanation:
        주어진 수 n 을 math module의 sqrt() method를 활용해 2부터 sqrt(n)까지 나눠보는 것으로 소수인지 확인한다.
    
    Variables:
        N : 주어진 수의 개수
        numbers : 주어진 수
        result : 소수의 개수
        base : 주어진 수가 소수인지 확인하기 위한 수, 2부터 base까지 주어진 수를 나눠보는 것으로 소수인지 확인한다.
        divide : 주어진 수를 나눠보는 수 list
        isprime : 주어진 수가 소수인지 아닌지 판단하기 위한 boolean type variable
    
    Example:
        >>> 4       : input N
        >>> 1 3 5 7 : input numbers
        >>> 3       : output result
    """
    N = int(input())
    numbers = list(map(int, input().split()))
    result = 0

    for num in numbers:
        if num == 1:
            continue
        base = int(math.sqrt(num))
        divide = [i for i in range(2, base+1)]
        isprime = True

        for div in divide:
            if num % div == 0:
                isprime = False
                break
            
        if isprime:
            result += 1

    print(result)

solution()