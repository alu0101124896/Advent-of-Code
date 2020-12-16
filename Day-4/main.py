file_name = input("\nInput file: ")

f = open(file_name, 'r')
passports = f.read().split("\n\n")

passports = list(
    map(lambda passport: passport.replace("\n", " ").split(" "), passports))

if passports[len(passports) - 1][len(passports[len(passports) - 1]) - 1] == "":
  passports[len(passports) - 1].pop()

passports = list(
    map(
        lambda passport: dict(
            map(lambda passport_field: tuple(passport_field.split(":")),
                passport)), passports))

valid_passports = list(
    map(
        lambda passport: True
        if ("byr" in passport.keys()) and ("iyr" in passport.keys()) and
        ("eyr" in passport.keys()) and ("hgt" in passport.keys()) and
        ("hcl" in passport.keys()) and ("ecl" in passport.keys()) and
        ("pid" in passport.keys()) else False, passports))

number_of_valid_passports = valid_passports.count(True)

print()
print("The number of valid passports is:", number_of_valid_passports)
