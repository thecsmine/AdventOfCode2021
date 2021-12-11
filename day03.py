from collections import defaultdict

bin_list = open("input03").readlines()
bin_list = list(map(lambda s:s.replace("\n", ""), bin_list))
freq_dict = defaultdict(int)
n = len(bin_list[0])

# Part 1
def f(digit):
    if digit == 0:
        return -1
    return 1

for string in bin_list:
    for k, digit in enumerate(string):
        freq_dict[k] += f(int(digit))

gamma = ""
epsilon = ""
for i in range(n):
    if freq_dict[i] > 0:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

# Part 2
def bit_criteria(lst, k):
    f_dict = defaultdict(int)
    for string in lst:
        f_dict[k] += f(int(string[k]))
    return f_dict

oxygen_list = [x for x in bin_list]
co2_list = [x for x in bin_list]
for i in range(n):
    oxygen_dict = bit_criteria(oxygen_list, i)
    co2_dict = bit_criteria(co2_list, i)
    if len(oxygen_list) != 1:
        if oxygen_dict[i] >= 0: # Most common bit is 1 (and if equally common)
            oxygen_list = [x for x in oxygen_list if x[i] == "1"]
        else:
            oxygen_list = [x for x in oxygen_list if x[i] == "0"]
    if len(co2_list) != 1:
        if co2_dict[i] >= 0: # Least common bit is 0 (and if equally common)
            co2_list = [x for x in co2_list if x[i] == "0"]
        else:
            co2_list = [x for x in co2_list if x[i] == "1"]
oxygen = oxygen_list[0]
co2 = co2_list[0]

print(f"Part 1: {int(gamma, base=2) * int(epsilon, base=2)} (gamma: {gamma}, epsilon: {epsilon})")
print(f"Part 2: {int(oxygen, base=2) * int(co2, base=2)} (oxygen: {oxygen}, co2: {co2})")