# 1
RED = "\u001b[41m"
WHITE = "\u001b[47m"
BLUE = '\u001b[44m'
END = "\u001b[0m"
print(f"{WHITE}{'   ' * 12}{END}")
print(f"{WHITE}{'   ' * 5}{RED}{'   ' * 2}{WHITE}{'   ' * 5}{END}")
print(f"{WHITE}{'   ' * 4}{RED}{'   ' * 4}{WHITE}{'   ' * 4}{END}")
print(f"{WHITE}{'   ' * 3}{RED}{'   ' * 6}{WHITE}{'   ' * 3}{END}")
print(f"{WHITE}{'   '  * 3}{RED}{'   ' * 6}{WHITE}{'   ' * 3}{END}")
print(f"{WHITE}{'   ' * 4}{RED}{'   ' * 4}{WHITE}{'   ' * 4}{END}")
print(f"{WHITE}{'   ' * 5}{RED}{'   ' * 2}{WHITE}{'   ' * 5}{END}")
print(f"{WHITE}{'   ' * 12}{END}")
# 2

print(f"{END}{'  ' * 2}{RED}{'  ' * 1}{END}{'  ' * 3}{RED}{'  ' * 1}{END}")
print(f"{END}{'  ' * 1}{RED}{'  ' * 1}{END}{'  ' * 1}{RED}{'  ' * 1}{END}{'  ' * 1}{RED}{'  ' * 1}{END}{'  ' * 1}{RED}{'  ' * 1}{END}")
print(f"{RED}{'  ' * 1}{END}{'  ' * 3}{RED}{'  ' * 1}{END}{'  ' * 3}{RED}{'  ' * 1}{END}")
print(f"{END}{'  ' * 1}{RED}{'  ' * 1}{END}{'  ' * 1}{RED}{'  ' * 1}{END}{'  ' * 1}{RED}{'  ' * 1}{END}{'  ' * 1}{RED}{'  ' * 1}{END}")
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
numb1 = numb2 = 0
for number in file:
    list.append(float(number))
file.close()
for i in range(len(list)):
    if -5 < list[i] < 0:
        numb1 += 1
    if list[i] < -5:
        numb2 += 1
print("Числа больше -5, но меньше 0","[", numb1, "]")
print(f'{RED}{" " * numb1}{END}')
print("Числа меньше -5","[", numb2, "]")
print(f'{BLUE}{" " * numb2}{END}')
