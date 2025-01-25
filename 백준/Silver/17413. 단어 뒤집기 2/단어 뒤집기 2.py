# 단어 뒤집기2
def main():
    S = input()
    answer = []
    tag_start = False
    temp = []
    for i in range(len(S)):
        if S[i] == "<":
            if temp:
                for j in range(len(temp) - 1, -1, -1):
                    answer.append(temp[j])
                temp.clear()
            tag_start = True
            answer.append(S[i])
        elif S[i] == ">":
            tag_start = False
            answer.append(S[i])
        else:
            if tag_start:
                answer.append(S[i])
            else:
                if i == len(S) - 1:
                    answer.append(S[i])
                    for j in range(len(temp) - 1, -1, -1):
                        answer.append(temp[j])
                    temp.clear()
                if S[i] == " ":
                    for j in range(len(temp) - 1, -1, -1):
                        answer.append(temp[j])
                    answer.append(S[i])
                    temp.clear()
                else:
                    temp.append(S[i])
    print("".join(answer))


if __name__ == "__main__":
    main()