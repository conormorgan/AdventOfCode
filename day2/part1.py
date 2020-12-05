with open("test.txt") as values:
    lines = values.read().splitlines()

valid_passwords = 0

for line in lines:
    splits = line.split()
    lower_limit = int(splits[0].split("-")[0])
    upper_limit = int(splits[0].split("-")[1])
    letter = splits[1][:1]
    password = splits[2]

    count = password.count(letter)

    if ((count >= lower_limit) and (count <= upper_limit)):
        valid_passwords += 1

print(valid_passwords)



