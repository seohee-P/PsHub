# 주몽
def main():
    N = int(input())
    M = int(input())
    ingredients = list(map(int, input().split()))
    ingredients.sort()
    answer = 0
    left, right = 0, N -1
    while left < right:
        temp = ingredients[left] + ingredients[right]
        if temp == M:
            answer += 1
            left += 1
            right -= 1
        elif temp < M:
            left += 1
        else:
            right -= 1
    print(answer)

if __name__=='__main__':
    main()