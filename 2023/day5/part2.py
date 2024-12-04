with open('day5\input.txt') as file:
    almanac = file.read().split("\n\n")

s = almanac[0].splitlines()[0].split(":")[-1].split()
#seeds = [int(x) for x in s]

def get_seed_ranges(sds):
    srs = []
    for i in range(1,len(sds),2):

        sd = int(s[i - 1])
        r = sd + int(s[i])

        srs.append((sd,r))

    return srs

seed_ranges = get_seed_ranges(s)

locations = []

for seed_range in seed_ranges:
    #print(f"seed range: {seed_range}")
    results = []
    for a in almanac:
        data = a.splitlines()
        if len(data) > 1:  
            #print(f"map: {data}")
            
            while seed_ranges:
                
                # sr = seed_ranges.pop()
                # start_range = sr[0]
                # end_range = sr[0] + sr[1]

                start_range, end_range = seed_ranges.pop()
                #print(f"start range {start_range}, end range {end_range}")

                for i in range(1, len(data)):
                    d,s,r = (int(x) for x in data[i].split()) # d,s,r
                    #print(d,s,r)
                    end_map = s + r
                    offset = d - s
                    if end_map <= start_range or end_range <= s:  # no overlap
                        continue
                    if start_range < s:
                        seed_ranges.append([start_range, s])
                        start_range = s
                    if end_map < end_range:
                        seed_ranges.append([end_map, end_range])
                        end_range = end_map
                    results.append([start_range + offset, end_range + offset])
                    break
                else:
                    results.append([start_range, end_range])
            seed_ranges = results
            results = []
    #print(seed_ranges)
    locations += seed_ranges
print(min(loc[0] for loc in locations))

# sample answer = 46    
# answer = 108956227
                