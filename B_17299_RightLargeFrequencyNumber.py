"""B 17299 오등큰수(Right Large Frequency Number)
Problem:
    크기가 N인 수열 A = A1, A2, ..., An 이 있다.
    수열의 각 원소 Ai에 대해서 오등큰수 NGF(i)를 구하려고 한다.
    Ai가 수열 A에서 등장한 횟수를 F(Ai)라고 했을 때, Ai의 오등큰수는 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다.
    그러한 수가 없는 경우에 오등큰수는 -1이다.

Input:
    첫째 줄에 수열 A의 크기 N(1 <= N <= 1,000,000)이 주어진다.
    둘째 줄에 수열 A의 원소 A1, A2, ..., An(1 <= Ai <= 1,000,000)이 주어진다.

Output:
    총 N개의 수 NGF(1), NGF(2), ..., NGF(N)을 공백으로 구분해 출력한다.
"""

def solution():
    """주어진 수열의 각 원소별 오등큰수를 구해 결과를 출력한다.
    Extra explanation:
        Stack을 이용한 풀이 방법은 오큰수와 동일하지만, 수열에서 원소의 등장 빈도수를 비교해야하는 점이 다르다.
        Counter Sort를 활용하여 수의 등장 빈도수를 비교한다.
    
    Variables:
        N : 주어진 수열의 크기
        sequence : 주어진 수열
        stack : 주어진 수열에서 오등큰수를 찾지 못한 원소의 index를 처리하기 위한 stack
        result : 주어진 수열의 오등큰수 list
        index : 주어진 수열에서 오등큰수를 찾지 못한 원소와 그 오른쪽에 있는 원소의 등장 빈도를 비교하기 위한 index
        count : 주어진 수열에서 각 원소의 등장 빈도수 list
    
    Example:
        >>> 7                   : input N
        >>> 1 1 2 3 4 2 1       : input sequence
        >>> -1 -1 1 2 2 1 -1    : output result
    """
    N = int(input())
    sequence = list(map(int, input().split()))
    result = [-1 for _ in range(N)]
    count = [0 for _ in range(max(sequence)+1)]
    stack = [0]
    index = 1

    for seq in sequence:
        count[seq] += 1
    while stack and index < N:
        while stack and count[sequence[stack[-1]]] < count[sequence[index]]:
            result[stack.pop()] = sequence[index]
        stack.append(index)
        index += 1
    
    for r in result:
        print(r, end=' ')
    
solution()