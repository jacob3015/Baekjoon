"""B 11726 2xn 타일링(2xn Tiling)
Problem:
    2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

Input:
    첫째 줄에 n이 주어진다.
    n은 1 이상 1,000 이하의 자연수이다.

Output:
    첫째 줄에 2xn 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.
"""

def solution():
    """2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구해 출력한다.
    Extra explanation:
        n = i일 때, i-1까지 타일이 채워졌다고 한다면, 타일을 채운는 방법의 수는 2x1 타일을 1개 추가하는 방법 뿐이다.
        n = i일 때, i-2까지 타일이 채워졌다고 한다면, 타일을 채우는 방법의 수는 1x2 타일을 2개 추가하는 방법 뿐이다.
        따라서, 타일을 채우는 방법의 수가 A(n) 일 때, A(n) = A(n-1) + A(n-2) (n>=3, A(1) = 1, A(2) = 2) 점화식을 만족한다.
        위 점화식을 dynamic programming의 memoization 기법을 활용해 bottom-up 방식으로 구현함으로 문제를 해결한다.

    Variables:
        n : 주어진 2xn 직사각형의 가로 길이
        tiles : 2xn 직사각형을 1x2, 2x1 타일로 채우는 방법의 수, dynamic programming memoization을 위한 list
    
    Example:
        >>> 9   : input n
        >>> 55  : output result
    """
    n = int(input())
    
    if n == 1 or n == 2:
        print(1) if n == 1 else print(2)
        return

    tiles = [0 for _ in range(n+1)]
    tiles[1], tiles[2] = 1, 2

    for i in range(3, n+1):
        tiles[i] = tiles[i-1] + tiles[i-2]

    print(tiles[n]%10007)

solution()