# --- Day 14: Reindeer Olympics ---

# Rdeers = [deer.split() for deer in open('input').readlines()]

rdeers = [[name, int(vel), int(limit), int(resttime),0, 0]
            for name, _,_, vel, _,_, limit, _,_,_,_,_,_, resttime,_ in (deer.split()
                for deer in open('input').readlines())
        ]
finaltime = 2503
elapsed = 0

while not elapsed == finaltime:
    for deer in rdeers:
        i = 0
        vel, limit, resttime = deer[1], deer[2], deer[3]
        while i < limit:
            if elapsed == finaltime: break
            deer[-1] += vel
            elapsed += 1
            i += 1
    
        tt = elapsed + resttime
        if tt > finaltime:
            elapsed -= tt - finaltime
            elapsed += resttime
        else: elapsed = tt
    
print(max(s[-1] for s in rdeers))

# for rdeer in Rdeers:
#     name, vel, limit, resttime = rdeer[0], int(rdeer[3]), int(rdeer[6]), int(rdeer[-2])
#     elapsed = 0
#     travelled = 0
#
#     while not elapsed == finaltime:
#         i = 0
#         while i < limit:
#             if elapsed == finaltime: break
#             travelled += vel
#             elapsed += 1
#             i += 1
#
#         tt = elapsed + resttime
#
#         if tt > finaltime:
#             elapsed -= tt - finaltime
#             elapsed += resttime
#         else: elapsed = tt
#
#     results.append([travelled])
#
# print(max(a[0] for a in results))

# --- Part Two ---

results = []
