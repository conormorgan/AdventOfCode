def getMostCommonBits(bins, bit, o2):

    if len(bins) == 1:
        return bins[0]
    else:
        ones = 0

        for bin in bins:
            if bin[bit] == "1":
                ones += 1
        
        if o2:
            if ones >= len(bins)/2:
                match = "1"
            else:
                match = "0"    
        else:
            if ones >= len(bins)/2:
                match = "0"
            else:
                match = "1"

        remaining = [bin for bin in bins if bin[bit] == match]

        bit += 1
        return getMostCommonBits(remaining, bit, o2)

with open('test.txt') as file:
    binary = file.read().splitlines()

size = len(binary[0])

o2 = int(getMostCommonBits(binary, 0, True),2)
print(o2)
co2 = int(getMostCommonBits(binary, 0, False),2)
print(co2)
print(o2*co2)


