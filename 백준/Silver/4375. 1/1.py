# 1
def main():
    while True:
        try:
            n = int(input())
        except:
            break
        now = 1
        answer = 1
        while now % n != 0:
            answer += 1
            now = now * 10 + 1
        print(answer)

if __name__ == '__main__':
    main()