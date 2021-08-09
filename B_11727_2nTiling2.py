"""B 11727 2xn 타일링 2(2xn Tiling 2)
Problem:
    2xn 직사각형을 1x2, 2x1, 2x2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

Input:
    첫째 줄에 n이 주어진다.
    n은 1 이상 1,000 이하이다.

Output:
    첫째 줄에 2xn 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
"""

def solution():
    """2xn 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 구해 출력한다.
    Extra explanation:
        Dynamic programming의 memoization 기법을 활용해 bottom-up 방식으로 문제를 해결한다.
        2xn 크기의 직사각형을 1x2, 2x1, 2x2 타일로 채우는 방법의 수를 A(n)이라고 할 때,
        n-1 까지 타일이 채워져 있다면, 타일을 채우는 방법은 2x1 타일로 남은 공간을 채우는 것이다.
        n-2 까지 타일이 채워져 있다면, 타일을 채우는 방법은 1x2 타일 2개 또는 2x2 타일 1개로 남은 공간을 채우는 것이다.
        따라서, A(n) = A(n-1) + (2 * A(n-2)) (n>=3, A(1) = 1, A(2) = 3)을 만족한다.

    Variables:
        n : 2xn 크기의 직사각형의 가로 길이
        tiles : 2xn 크기의 직사각형을 채우는 방법의 수, Memoization을 위한 list
    
    Example:
        >>> 8       : input n
        >>> 171     : output result
    """
    n = int(input())

    if n == 1 or n == 2:
        print(1) if n == 1 else print(3)
        return

    tiles = [0 for _ in range(n+1)]
    tiles[1], tiles[2] = 1, 3

    for i in range(3, n+1):
        tiles[i] = tiles[i-1] + (2 * tiles[i-2])
        
    print(tiles[n]%10007)

solution()