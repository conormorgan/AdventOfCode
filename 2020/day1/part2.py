# Find the 3 values that sum to 2020 and multiply them

with open('test.txt') as file:
    values = file.read().splitlines()

int_values = [int(x) for x in values]

for x in int_values:
    for y in int_values:
        for z in int_values:
            if (x+y+z == 2020):
                print(x)
                print(y)
                print(z)
                print(x*y*z)