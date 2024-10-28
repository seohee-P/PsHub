# 주몽
def main():
    N = int(input())
    M = int(input())
    ingredients = sorted(list(map(int, input().split())))
    answer = 0
    for i in range(N):
        if M - ingredients[i] <= 0 or ingredients[i] == 0:
            continue
        if ingredients.count(M - ingredients[i]) != 0:
            index = ingredients.index(M - ingredients[i])
            if i == index:
                continue
            ingredients[index] = 0
            ingredients[i] = 0
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()