"""B 2193 이친수(Pinary Number)
Problem:
    0과 1로만 이루어진 수를 이진수라 한다.
    이러한 이진수 중 특별한 성질을 갖는 것들이 있는데, 이들을 이친수(pinary number)라 한다.
    이친수는 다음의 성질을 만족한다.
    1. 이친수는 0으로 시작하지 않는다.
    2. 이친수에서는 1이 두번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.
    N(1 <= N <= 90)이 주어졌을 때, N자리 이친수의 개수를 구하는 프로그램을 작성하시오.

Input:
    첫째 줄에 N이 주어진다.

Output:
    첫째 줄에 N자리 이친수의 개수를 출력한다.
"""

def solution():
    """N자리 이친수의 개수를 구해 출력한다.
    Extra explanation:
        i-1자리의 수가 이친수이며, i-1번째 수가 0일 때, i번째 수가 1또는 0이면 i자리의 수는 이친수이다.
        i-1자리의 수가 이친수이며, i-1번째 수가 1일 때, i번째 수가 0이면 i자리의 수는 이친수이다.
        이를 풀이하면, i번째 수가 0이 되는 경우는 i-1번째 수가 1또는 0일 때이며, i번째 수가 1이 되는 경우는 i-1번째 수가 0일 때이다.
        위 풀이를 만족하도록 dynamic programming의 memoization 기법을 활용해 bottom-up 방식으로 문제를 해결한다.
    
    Variables:
        N : 이친수의 자리수
        pinary : N자리 이친수의 개수 list, 2차원 list이며 pinary[자리수][마지막자리의 수]를 만족한다. 예를 들어, pinary[3][0] = 3자리이며 3번째 자리의 수가 0인 이친수의 개수이다.
    
    Example:
        >>> 5   : input N
        >>> 5   : output result
    """
    N = int(input())

    if N < 3:
        print(1)
        return

    pinary = [[0]*2 for _ in range(N+1)]
    pinary[1][1] = pinary[2][0] = 1

    for i in range(3, N+1):
        for j in range(2):
            if j < 1:
                pinary[i][j] = pinary[i-1][j] + pinary[i-1][j+1]
            else:
                pinary[i][j] = pinary[i-1][j-1]
                
    print(sum(pinary[N]))

solution()