"""Problem : B 10828 스택(Stack)

정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
명령은 총 다섯 가지이다.
1. push X : 정수 X를 스택에 넣는 연산이다.
2. pop : 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
3. size : 스택에 들어있는 정수의 개수를 출력한다.
4. empty : 스택이 비어있으면 1, 아니면 0을 출력한다.
5. top : 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

첫째 줄에 주어지는 명령의 수 N(1 <= N <= 10,000)이 주어진다.
둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다.
문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
"""

def solution():
    """정수를 저장하는 스택에서 5가지 명령을 처리한다.

    Variables:
        N : 입력 명령의 수
        command : 입력된 명령 list
        stack : 정수를 저장하는 stack
    
    Example:
        >>> 5           : input N
        >>> push 123    : input command 1
        >>> top         : input command 2
        >>> size        : input command 3
        >>> pop         : input command 4
        >>> empty       : input command 5
        >>> 123         : output top command result
        >>> 1           : output size command result
        >>> 123         : output pop command result
        >>> 1           : output empty command result
    """
    N = int(input())
    command = [input() for _ in range(N)]
    stack = []
    for com in command:
        if len(com) > 5:
            stack.append(int(com[5:]))
        elif com == 'pop':
            if not stack:
                print(-1)
            else:
                print(stack.pop())
        elif com == 'size':
            print(len(stack))
        elif com == 'empty':
            if not stack:
                print(1)
            else:
                print(0)
        else:
            if not stack:
                print(-1)
            else:
                print(stack[-1])

solution()