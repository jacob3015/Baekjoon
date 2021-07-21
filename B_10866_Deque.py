"""B 10866 덱(Deque)
Problem:
    정수를 저장하는 Deque을 구현한 다음 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
    명령은 아래 8가지이다.
    1. push_front X : 정수 X를 deque의 앞에 넣는다.
    2. push_back X : 정수 X를 deque의 뒤에 넣는다.
    3. pop_front : Deque의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. Deque이 비어있다면 -1을 출력한다.
    4. pop_back : Deque의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. Deque이 비어있다면 -1을 출력한다.
    5. size : Deque에 들어있는 정수의 개수를 출력한다.
    6. empty : Deque이 비어있으면 1을 아니면 0을 출력한다.
    7. front : Deque의 가장 앞에 있는 정수를 출력한다. Deque이 비어있다면 -1을 출력한다.
    8. back : Deque의 가장 뒤에 있는 정수를 출력한다. Deque이 비어있다면 -1을 출력한다.

Input:
    첫째 줄에 주어지는 명령의 수 N(1 <= N <= 10,000)이 주어진다.
    둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
    문제에 나와있지 않은 명령이 주어지는 경우는 없다.

Output:
    출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
"""
import sys
from collections import deque

def solution():
    """Deque로 구현한 queue를 이용해 명령어를 처리한 뒤 결과를 출력한다.
    Extra explanation:
        시간 제한을 만족하기 위해 입력은 sys.stdin.readline() method를 사용한다.

    Variables:
        N : 명령어의 개수
        commands : 주어진 명렁어 list
        queue : Deque로 구현한 queue
    
    Example:
        >>> 8               : input N
        >>> push_back 1     : input commands
        >>> push_front 2
        >>> size
        >>> empty
        >>> front
        >>> back
        >>> pop_front
        >>> pop_back
        >>> 2               : outputs
        >>> 0
        >>> 2
        >>> 1
        >>> 2
        >>> 1
    """
    N = int(sys.stdin.readline().rstrip())
    commands = [sys.stdin.readline().rstrip() for _ in range(N)]
    queue = deque()
    for comm in commands:
        if comm == 'size':
            print(len(queue))
        elif comm == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif comm == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif comm == 'back':
            if queue:
                print(list(queue)[-1])
            else:
                print(-1)
        elif comm[4] == 'f':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif comm[4] == 'b':
            if queue:
                print(queue.pop())
            else:
                print(-1)
        elif comm[5] == 'f':
            queue.appendleft(comm[11:])
        else:
            queue.append(comm[10:])

solution()