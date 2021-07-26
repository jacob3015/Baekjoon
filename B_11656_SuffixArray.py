"""B 11656 접미사 배열(Suffix Array)
Problem:
    접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬해 놓은 배열이다.
    baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지가 있다.
    이를 사전순으로 정렬하면 aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon이 된다.
    문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성하시오.

Input:
    첫째 줄에 문자열 S가 주어진다.
    S는 알파벳 소문자로만 이루어져 있고, 길이는 1,000보다 작거나 같다.

Output:
    첫째 줄부터 S의 접미사를 사전순으로 한 줄에 하나씩 출력한다.
"""

def solution():
    """주어진 문자열의 모든 접미사를 사전순으로 정렬해 출력한다.
    Extra explanation:
        Stack을 활용해 주어진 문자열의 모든 접미사를 구한 뒤 사전 순으로 정렬한다.
    
    Variables:
        string : 주어진 문자열
        result : 주어진 문자열 string의 모든 접미사를 사전 순으로 정렬한 list

    Example:
        >>> baekjoon    : input string
        >>> aekjoon     : outputs
        >>> baekjoon
        >>> ekjoon
        >>> joon
        >>> kjoon
        >>> n
        >>> on
        >>> oon
    """
    string = list(input())[::-1]
    result = []

    for _ in range(len(string)):
        result.append(''.join(string[::-1]))
        string.pop()

    result.sort()

    for res in result:
        print(res)

solution()