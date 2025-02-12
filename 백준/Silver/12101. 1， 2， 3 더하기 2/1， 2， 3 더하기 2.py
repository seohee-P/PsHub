# 1, 2, 3 더하기 2
def main():
    n, k = map(int, input().split())
    dp = [0, 1, 2, 4]

    for i in range(4, n + 1):
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])

    if k > dp[n]:
        print(-1)
        return

    else:
        sum3_list = ["1+1+1", "1+2", "2+1", "3"]
        sum2_list = ["1+1", "2"]
        sum1_list = ["1"]
        answer = ""
        while n >= 4:
            if 0 < k <= dp[n-1]:
                answer += "1+"
                n -= 1
            elif dp[n-1] < k <= dp[n] - dp[n-3]:
                answer += "2+"
                k -= dp[n-1]
                n -= 2
            elif dp[n] - dp[n-3] < k <= dp[n]:
                answer += "3+"
                k -= (dp[n-2] + dp[n-1])
                n -= 3

        if n == 3:
            answer += sum3_list[k-1]
        elif n == 2:
            answer += sum2_list[k-1]
        elif n == 1:
            answer += sum1_list[k-1]
        print(answer)

if __name__ == "__main__":
    main()