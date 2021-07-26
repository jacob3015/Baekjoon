"""B 2743 단어 길이 재기(Measure Word Length)
Problem:
    알파벳으로만 이루어진 단어를 입력받아, 그 길이를 출력하는 프로그램을 작성하시오.

Input:
    첫째 줄에 영어 소문자와 대문자로만 이루어진 단어가 주어진다.
    단어의 길이는 최대 100이다.

Output:
    첫째 줄에 입력으로 주어진 단어의 길이를 출력한다.
"""

def solution():
    """주어진 단어의 길이를 출력한다.
    Example:
        >>> baekjoon    : input word
        >>> 8           : output word length
    """
    print(len(input()))

solution()