"""Problem : B 1874 스택 수열(Stack Sequence)

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
이 때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다.
이를 계산하는 프로그램을 작성하라.

첫 줄에 n(1 <= n <= 100,000)이 주어진다.
둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다.
push 연산은 + 로, pop 연산은 - 로 표현하도록 한다. 불가능한 경우 NO를 출력한다.
"""

def solution():
    """Stack에 1부터 n까지의 수를 넣어다가 뽑아 놓음으로써 주어진 수열을 만들 수 있는지 계산해 결과를 출력한다.
    
    Variables:
        n : 1부터 n까지의 정수에서 n
        sequence : 주어진 수열 list
        stack : push, pop 연산을 통해 주어진 수열을 만들기 위한 list
        operations : push 연산과 pop 연산을 기록하기 위한 list
        sequence_iter : sequence list iterator
        number : 1부터 n까지의 정수
    
    Example:
        >>> 4   : input n
        >>> 3   : input sequence
        >>> 4
        >>> 2
        >>> 1
        >>> +   : output operations
        >>> +
        >>> +
        >>> -
        >>> +
        >>> -
        >>> -
        >>> -
    """
    n = int(input())
    sequence = [int(input()) for _ in range(n)]
    stack = []
    operations = []
    sequence_iter = 0

    for number in range(1, n+1):
        stack.append(number)
        operations.append('+')
        while sequence[sequence_iter] == stack[-1]:
            stack.pop()
            operations.append('-')
            sequence_iter += 1
            if sequence_iter >= n or not stack:
                break

    if not stack:
        for oper in operations:
            print(oper)
    else:
        print('NO')

solution()