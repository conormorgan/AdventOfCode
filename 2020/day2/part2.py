with open("test.txt") as values:
    lines = values.read().splitlines()

valid_passwords = 0

for line in lines:
    splits = line.split()
    first_pos = int(splits[0].split("-")[0]) - 1
    second_pos = int(splits[0].split("-")[1]) - 1
    letter = splits[1][:1]
    password = splits[2]


    if (password[first_pos] == letter or password[second_pos] == letter):
        if password[first_pos] != password[second_pos]:
            valid_passwords += 1

print(valid_passwords)