file_name = input("\nInput file: ")

f = open(file_name, 'r')
num_list = f.read().split("\n")

if num_list[len(num_list) - 1] == '':
  num_list.pop()
num_list = list(map(int, num_list))

winers = []
for i in range(len(num_list)):
  for j in range(i + 1, len(num_list)):
    if (num_list[i] + num_list[j]) == 2020:
      winers.append(num_list[i])
      winers.append(num_list[j])

print()
print(winers[0], '+', winers[1], "=", winers[0] + winers[1])
print(winers[0], '*', winers[1], "=", winers[0] * winers[1])

winers = []
for i in range(len(num_list)):
  for j in range(i + 1, len(num_list)):
    for k in range(j + 1, len(num_list)):
      if (num_list[i] + num_list[j] + num_list[k]) == 2020:
        winers.append(num_list[i])
        winers.append(num_list[j])
        winers.append(num_list[k])

print()
print(winers[0], '+', winers[1], '+', winers[2], "=",
      winers[0] + winers[1] + winers[2])
print(winers[0], '*', winers[1], '*', winers[2], "=",
      winers[0] * winers[1] * winers[2])
print()
