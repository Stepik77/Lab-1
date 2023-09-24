# 1
RED = "\u001b[41m"
WHITE = "\u001b[47m"
BLUE = '\u001b[44m'
END = "\u001b[0m"
for i in range(9):
    if i == 0:
        print(f"{WHITE}{'  ' * 12}{END}")
    if i == 1:
        print(f"{WHITE}{'  ' * 5}{RED}{'  ' * 2}{WHITE}{'  ' * 5}{END}")
    if i == 2:
        print(f"{WHITE}{'  ' * 4}{RED}{'  ' * 4}{WHITE}{'  ' * 4}{END}")
    if i == 3:
        print(f"{WHITE}{'  ' * 3}{RED}{'  ' * 6}{WHITE}{'  ' * 3}{END}")
    if i == 4:
        print(f"{WHITE}{'  ' * 3}{RED}{'  ' * 6}{WHITE}{'  ' * 3}{END}")
    if i == 5:
        print(f"{WHITE}{'  ' * 4}{RED}{'  ' * 4}{WHITE}{'  ' * 4}{END}")
    if i == 6:
        print(f"{WHITE}{'  ' * 5}{RED}{'  ' * 2}{WHITE}{'  ' * 5}{END}")
    if i == 7:
        print(f"{WHITE}{'  ' * 12}{END}")
# 2
for i in range(5):
    if i == 1:
        print(f"{END}{'  ' * 2}{RED}{'  ' * 1}{END}{'  ' * 3}{RED}{'  ' * 1}{END}")
    if i == 2:
        print(f"{END}{'  ' * 1}{RED}{'  ' * 1}{END}{'  ' * 1}{RED}{'  ' * 1}{END}{'  ' * 1}{RED}{'  ' * 1}{END}{'  ' * 1}{RED}{'  ' * 1}{END}")
    if i == 2:
        print(f"{RED}{'  ' * 1}{END}{'  ' * 3}{RED}{'  ' * 1}{END}{'  ' * 3}{RED}{'  ' * 1}{END}")
    if i == 3:
        print(f"{END}{'  ' * 1}{RED}{'  ' * 1}{END}{'  ' * 1}{RED}{'  ' * 1}{END}{'  ' * 1}{RED}{'  ' * 1}{END}{'  ' * 1}{RED}{'  ' * 1}{END}")
    if i == 4:
        print(f"{END}{'  ' * 2}{RED}{'  ' * 1}{END}{'  ' * 3}{RED}{'  ' * 1}{END}")
# 3
plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i * 3

step = round(abs(result[0] - result[9]) / 9, 2)
print(step)

for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = step * (8 - i) + step

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k + 1] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '!!'
    print(line)
print('\t0\t1 2 3 4 5 6 7 8 9')
# 4
file = open("sequence.txt", "r")
list = []
q = 0
w = 0
for number in file:
    list.append(float(number))
    s = list
file.close()
for i in range(len(s)):
    if -5 < s[i] < 0:
        q += 1
    if s[i] < -5:
        w += 1
print("Числа больше -5, но меньше 0","[", q, "]")
print(f'{RED}{" " * q}{END}')
print("Числа меньше -5","[", w, "]")
print(f'{BLUE}{" " * w}{END}')

