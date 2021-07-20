"""Problem : B 1158 요세푸스 문제(Josephus Problem)

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(<=N)가 주어진다.
이제 순서대로 K번째 사람을 제거한다.
한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
원에서 사람들이 제거되는 순서를 (N, K) - 요세푸스 순열이라고 한다.
N과 K가 주어지면 (N, K) - 요세푸스 순열을 구하는 프로그램을 작성하시오.

첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다.(1 <= K <= N <= 5,000)

결과로 요세푸스 순열을 출력한다.
"""
from collections import deque

def solution():
    """주어진 N, K와 deque로 구현한 queue를 사용해 요세푸스 순열을 구해 출력한다.

    Variables:
        N : 1부터 N까지의 정수 N
        K : 양의 정수 K
        queue : 1부터 N까지의 수열, deque로 구현한 queue
        josephus : (N, K) - 요세푸스 순열
    
    Example:
        >>> 7 3                     : input N, K
        >>> <3, 6, 2, 7, 5, 1, 4>   : output (N, K) - Josephus Permutation
    """
    N, K = map(int, input().split())
    queue = deque([i for i in range(1, N+1)])
    josephus = []

    for _ in range(N):
        for _ in range(K-1):
            queue.append(queue.popleft())
        josephus.append(queue.popleft())

    print('<', end='')
    for iter in range(len(josephus)):
        if josephus[iter] != josephus[-1]:
            print(f'{josephus[iter]},', end=' ')
        else:
            print(f'{josephus[iter]}>')

solution()