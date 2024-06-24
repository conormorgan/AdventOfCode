with open('day2\input.txt') as file:
    game_stats = file.read().splitlines()

games = {}

for game in game_stats:

    game_id, game_info = game.split(":")
    gid = game_id.split()[-1]

    cube_stats = {}

    rounds = game_info.split(";")
    for round in rounds:
        cubes = round.split(",")

        for cube in cubes:
            count_char, colour = cube.split()

            count = int(count_char)

            if colour in cube_stats.keys():
                if count > cube_stats[colour]:
                    cube_stats[colour] = count
            
            else:
                cube_stats[colour] = count
    
    games[gid] = cube_stats

powers = [g["red"] * g["green"] * g["blue"] for g in games.values()]

print(sum(powers))