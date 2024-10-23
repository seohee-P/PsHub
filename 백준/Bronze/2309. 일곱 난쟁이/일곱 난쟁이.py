# 일곱 난쟁이
def main():
    dwarves = sorted([int(input()) for _ in range(9)])

    def find_wrong_dwarf():
        while True:
            for i in range(9):
                for j in range(i + 1, 9):
                    if sum(dwarves) - dwarves[i] - dwarves[j] == 100:
                        return i, j

    wrong_dwarf1, wrong_dwarf2 = find_wrong_dwarf()
    for i in range(9):
        if i != wrong_dwarf1 and i != wrong_dwarf2:
            print(dwarves[i])


if __name__ == '__main__':
    main()