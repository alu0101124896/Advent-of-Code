passports = open(input("\nInput file: "), 'r').read().split("\n\n")

passports = list(
    map(lambda passport: passport.replace("\n", " ").split(" "), passports))

if passports[len(passports) - 1][len(passports[len(passports) - 1]) - 1] == "":
  passports[len(passports) - 1].pop()

passports = list(
    map(
        lambda passport: dict(
            map(lambda passport_field: tuple(passport_field.split(":")),
                passport)), passports))


def is_int(number):
  try:
    int(number)
    return True
  except ValueError:
    return False


def is_hex(number):
  try:
    int(number, 16)
    return True
  except ValueError:
    return False


valid_passports = list(
    map(
        lambda passport: True if ("byr" in passport.keys()) and
        (1920 <= int(passport.get("byr")) <= 2002) and
        ("iyr" in passport.keys()) and
        (2010 <= int(passport.get("iyr")) <= 2020) and
        ("eyr" in passport.keys()) and
        (2020 <= int(passport.get("eyr")) <= 2030) and
        ("hgt" in passport.keys()) and (
            ("cm" in passport.get("hgt") and 150 <= int(
                passport.get("hgt").strip("cm")) <= 193) or
            ("in" in passport.get("hgt") and 59 <= int(
                passport.get("hgt").strip("in")) <= 76)) and
        ("hcl" in passport.keys()) and
        (passport.get("hcl").startswith("#") and len(passport.get("hcl")) == 7
         and is_hex(passport.get("hcl").strip("#"))) and
        ("ecl" in passport.keys()) and (passport.get(
            "ecl") in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]) and
        ("pid" in passport.keys()) and (len(passport.get("pid")) == 9 and
                                        is_int(passport.get("pid"))) else False,
        passports))

number_of_valid_passports = valid_passports.count(True)

print("\nThe number of valid passports is:", number_of_valid_passports)
