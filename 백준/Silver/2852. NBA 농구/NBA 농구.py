# NBA 농구
def main():
    N = int(input())
    score1, score2 = 0, 0
    was_winner, time1, time2 = 0, 0, 0
    answer = [[0, 0], [0, 0]]
    for _ in range(N):
        now_winner = was_winner
        team, time = input().split()
        if team == '1':
            score1 += 1
        else:
            score2 += 1
        if score1 > score2:
            now_winner = 1
        elif score2 > score1:
            now_winner = 2
        else:
            now_winner = 0
        if now_winner == was_winner:
            continue
        if now_winner == 1:
            time1 = time
            if was_winner == 2:
                m1, s1 = time1.split(':')
                m2, s2 = time2.split(':')
                answer[1][0] += int(m1) - int(m2)
                answer[1][1] += int(s1) - int(s2)
        if now_winner == 2:
            time2 = time
            if was_winner == 1:
                m1, s1 = time1.split(':')
                m2, s2 = time2.split(':')
                answer[0][0] += int(m2) - int(m1)
                answer[0][1] += int(s2) - int(s1)
        if now_winner == 0:
            now_winner = 0
            if was_winner == 1:
                m1, s1 = time.split(':')
                m2, s2 = time1.split(':')
                answer[0][0] += int(m1) - int(m2)
                answer[0][1] += int(s1) - int(s2)
            if was_winner == 2:
                m1, s1 = time2.split(':')
                m2, s2 = time.split(':')
                answer[1][0] += int(m2) - int(m1)
                answer[1][1] += int(s2) - int(s1)
        was_winner = now_winner
    if was_winner == 1:
        m1, s1 = time1.split(':')
        answer[0][0] += 48 - int(m1)
        answer[0][1] += 0 - int(s1)
    if was_winner == 2:
        m2, s2 = time2.split(':')
        answer[1][0] += 48 - int(m2)
        answer[1][1] += 0 - int(s2)
    answer[0][0] += answer[0][1] // 60
    answer[0][1] = answer[0][1] % 60
    answer[1][0] += answer[1][1] // 60
    answer[1][1] = answer[1][1] % 60

    print("{0:02d}".format(answer[0][0]) + ":" + "{0:02d}".format(answer[0][1]))
    print("{0:02d}".format(answer[1][0]) + ":" + "{0:02d}".format(answer[1][1]))


if __name__ == '__main__':
    main()