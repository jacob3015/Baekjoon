"""B 17087 숨바꼭질 6(Hide and Seek 6)
Problem:
    수빈이는 동생 N 명과 숨바꼭질을 하고 있다.
    수빈이는 현재 점 S 에 있고, 동생은 A1, A2, ..., An 에 있다.
    수빈이는 걸어서 이동할 수 있다.
    수빈이의 위치가 X 일때 걷는다면 1 초 후에 X+D 나 X-D 로 이동할 수 있다.
    수빈이의 위치가 동생이 있는 위치와 같으면, 동생을 찾았다고 한다.
    모든 동생을 찾기 위해 D의 값을 정하려고 한다.
    가능한 D 의 최댓값을 구해보자.

Input:
    첫째 줄에 N 과 S 가 주어진다. N 은 1 이상 10^5 이하이며, S 는 1 이상 10^9 이하이다.
    둘째 줄에 동생의 위치 Ai 가 주어진다. Ai는 1 이상 10^9 이하이다.
    동생의 위치는 모두 다르며, 수빈이의 위치와 같지 않다.

Output:
    가능한 D 값의 최댓값을 출력한다.
"""
import math

def solution():
    """수빈이와 동생들 사이의 거린 d를 구한 뒤 모든 d의 최대공약수 중 최솟값을 구해 출력한다.

    Variables:
        N : 동생들의 수
        S : 수빈이의 위치
        brothers : 동생들의 위치
        result : 수빈이와 모든 동생 사이의 거리 d의 최대 공약수 중 최솟값
    
    Example:
        >>> 3 81        : input N, S
        >>> 33 105 57   : input brother's locations
        >>> 24          : output result
    """
    N, S = map(int, input().split())
    brothers = list(map(int, input().split()))

    for i in range(N):
        brothers[i] -= S
        if brothers[i] < 0:
            brothers[i] *= (-1)

    result = brothers[0]

    for d in brothers:
        if math.gcd(result, d) < result:
            result = math.gcd(result, d)
            
    print(result)

solution()