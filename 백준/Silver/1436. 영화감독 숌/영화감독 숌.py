# 영화감독 숌
def main():
    N = int(input())
    if N == 1:
        print(666)
        return
    find_c = 1
    while True:
        temp = pow(10, find_c - 1) + 9 * pow(10, find_c - 2) * (find_c - 1)
        if temp >= N:
            break
        find_c += 1

    answer = []
    for i in range(find_c):
        # '666'이 제일 앞에 위치
        if i == 0:
            for j in range(pow(10, find_c - 1)):
                answer.append('666' + "{0:0{1}d}".format(j, find_c - 1))
        elif i == find_c - 1:
            for j in range(pow(10, find_c - 1)):
                answer.append("{0:0{1}d}".format(j, find_c - 1) + '666')
        else:
            for j in range(pow(10, i)):
                result = "{0:0{1}d}".format(j, i) + '666'
                for k in range(pow(10, find_c - 1 - i)):
                    answer.append(result + "{0:0{1}d}".format(k, find_c - i - 1))

    answer = sorted(list(set(answer)))
    print(int(answer[N - 1]))


if __name__ == '__main__':
    main()
