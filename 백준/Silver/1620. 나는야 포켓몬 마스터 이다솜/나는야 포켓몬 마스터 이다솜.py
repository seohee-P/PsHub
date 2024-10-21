# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    nameKey = dict()
    numberKey = dict()
    for i in range(1, N+1):
        name = input().strip()
        nameKey[name] = i
        numberKey[i] = name
    for i in range(M):
        question = input().strip()
        if question.isdigit():
            print(numberKey[int(question)])
        else:
            print(nameKey[question])

main()