"""B 1929 소수 구하기(Calculate Prime Number)
Problem:
    M 이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하시오.

Input:
    첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다.
    M과 N은 1 이상 1,000,000 이하의 자연수이며, M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

Output:
    한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
"""
import math

def solution():
    """M 이상 N 이하의 수 중 소수를 찾아 출력한다.

    Variables:
        M, N : M 이상 N 이하의 소수를 찾기 위한 두 개의 자연수
        prime : M 이상 N 이하의 소수 list
        base : 2부터 math.sqrt(number)까지 number를 나눠보는 것으로 number가 소수 인지 찾기 위한 수
        isprime : 소수라면 True, 아니라면 False 값을 저장하는 boolean type variable
    
    Example:
        >>> 3 16    : input M, N
        >>> 3       : ouputs
        >>> 5
        >>> 7
        >>> 11
        >>> 13
    """
    M, N = map(int, input().split())
    prime = []

    for number in range(M, N+1):
        if number == 1:
            continue
        base = int(math.sqrt(number))
        isprime = True

        for divide in range(2, base+1):
            if number % divide == 0:
                isprime = False
                break

        if isprime:
            prime.append(number)
            
    for num in prime:
        print(num)

solution()