from collections import defaultdict

bin_list = open("input03").readlines()
bin_list = list(map(lambda s:s.replace("\n", ""), bin_list))
freq_dict = defaultdict(int)
n = len(bin_list[0])

def f(digit):
    if digit == 0:
        return -1
    return 1

for string in bin_list:
    for k, digit in enumerate(string):
        freq_dict[n - 1 - k] += f(int(digit))

gamma = ""
epsilon = ""
for i in range(n):
    if freq_dict[n - 1 - i] > 0:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(int(gamma, base=2) * int(epsilon, base=2))