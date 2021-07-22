"""B 17298 오큰수(Right Large Number)
Problem:
    크기가 N인 수열 A = A1, A2, ..., An 이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
    Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다.
    그러한 수가 없는 경우에 오큰수는 -1이다.

Input:
    첫째 줄에 수열 A의 크기 N(1 <= N <= 1,000,000)이 주어진다.
    둘째에 수열 A의 원소 A1, A2, ..., An 이 주어진다.

Output:
    총 N개의 수 NGE(1), NGE(2), ..., NGE(N) 을 공백으로 구분해 출력한다.
"""

def solution():
    """Stack을 사용해 주어진 수열의 오큰수를 찾아 결과를 출력한다.

    Variables:
        N : 주어진 수열의 크기
        sequence : 주어진 수열
        stack : 수열 sequence에서 오큰수를 찾지 못한 수의 index
        result : 결과 list
        index : 수열 sequence에서 오큰수를 찾지 못한 수보다 오른쪽에 있는 수의 indexs

    Example:
        >>> 4           : input N
        >>> 3 5 2 7     : input sequence
        >>> 5 7 7 -1    : output result
    """
    N = int(input())
    sequence = list(map(int, input().split()))
    stack = [0]
    result = [-1 for _ in range(N)]
    index = 1

    while stack and index < N:
        while stack and sequence[stack[-1]] < sequence[index]:
            result[stack.pop()] = sequence[index]
        stack.append(index)
        index += 1
    
    for r in result:
        print(r, end=' ')
    
solution()