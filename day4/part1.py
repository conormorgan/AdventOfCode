with open("test.txt") as f:
    passports = f.read().split("\n\n")

valid = 0
fields = ["byr","iyr","eyr", "hgt","hcl" ,"ecl","pid","cid"]
for p in passports:
    passport = {}
    p = p.replace("\n"," ")
    fields = p.split(" ")
    for field in fields:
        key_value = field.split(":")
        passport[key_value[0]] = key_value[1]
    
    if (len(passport.keys()) == 8) :
        valid += 1
    elif ((len(passport.keys()) == 7) and ("cid" not in passport.keys())):
        valid += 1

print(valid)


