file_name = input("\nInput file: ")

f = open(file_name, 'r')
password_list = f.read().split("\n")

if password_list[len(password_list) - 1] == '':
  password_list.pop()


def formatPassword(password):
  formatedPassword = password.split()
  formatedPassword[0] = formatedPassword[0].split("-")
  formatedPassword[1] = formatedPassword[1].strip(":")
  return formatedPassword


def checkPassword(password):
  num_of_chars = password[2].count(password[1])
  return (int(password[0][0]) <= num_of_chars) and (num_of_chars <= int(
      password[0][1]))


password_list = list(map(formatPassword, password_list))
valid_passwords = list(map(checkPassword, password_list))
num_of_valid_passwords = valid_passwords.count(True)

print("Number of valid passwords:", num_of_valid_passwords)


def checkPasswordV2(password):
  first = password[2][int(password[0][0]) - 1] == password[1]
  second = password[2][int(password[0][1]) - 1] == password[1]

  return not (first and second) and (first or second)


valid_passwords_v2 = list(map(checkPasswordV2, password_list))
num_of_valid_passwords_v2 = valid_passwords_v2.count(True)

print("Number of valid passwords (V2):", num_of_valid_passwords_v2)
