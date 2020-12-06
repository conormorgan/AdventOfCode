with open("test.txt") as f:
    passports = f.read().split("\n\n")

def passport_valid(p):

    valid = True

    for key in p.keys():
        if valid:
            if key == "byr":
                if (len(p[key]) != 4) or (int(p[key]) < 1920) or (int(p[key]) > 2002):
                    valid = False
            if key == "iyr":
                if (len(p[key]) != 4) or (int(p[key]) < 2010) or (int(p[key]) > 2020):
                    valid = False
            if key == "eyr":
                if (len(p[key]) != 4) or (int(p[key]) < 2020) or (int(p[key]) > 2030):
                    valid = False
            if key == "hgt":
                if p[key][-2:] == "cm":
                    if (int(p[key][:-2]) < 150) or (int(p[key][:-2]) > 193):
                        valid = False
                elif p[key][-2:] == "in":
                    if (int(p[key][:-2]) < 59) or (int(p[key][:-2]) > 76):
                        valid = False
                else:
                    valid = False
            if key == "hcl":
                if (len(p[key]) == 7) and (p[key][0] == "#"):
                    try:
                        int(p[key][1:],16)
                    except ValueError:
                        valid = False
                else:
                    valid = False
            if key == "ecl":
                if p[key] not in ["amb", "blu", "brn", "gry", "grn", "hzl","oth"]:
                    valid = False
            if key == "pid":
                if (len(p[key]) != 9) or (not p[key].isdigit()):
                    valid = False


    return valid


valid = 0

for p in passports:
    passport = {}
    p = p.replace("\n"," ")
    fields = p.split(" ")
    for field in fields:
        key_value = field.split(":")
        passport[key_value[0]] = key_value[1]
    
    if (len(passport.keys()) == 8) :
        if passport_valid(passport):
            valid += 1
    elif ((len(passport.keys()) == 7) and ("cid" not in passport.keys())):
        if passport_valid(passport):
            valid += 1

print(valid)


