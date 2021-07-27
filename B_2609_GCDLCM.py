"""B 2609 최대공약수와 최소공배수(GCD and LCM)
Problem:
    두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

Input:
    첫째 줄에는 두 개의 자연수가 주어진다.
    이 둘은 10,000 이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

Output:
    첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
"""
import math

def solution():
    """주어진 두 자연수의 최대 공약수와 최소 공배수를 구해 출력한다.

    Variables:
        num1, num2 : 주어진 두개의 자연수
    
    Example:
        >>> 24, 18  : input
        >>> 6       : output gcd
        >>> 72      : output lcm
    """
    num1, num2 = map(int, input().split())
    print(math.gcd(num1, num2))
    print(math.lcm(num1, num2))

solution()