# where b in the pickle
for ini, i in enumerate(b):
    name = i[0]
    name_values = i[1]
    for jnj, j in enumerate(name_values):
        number = j[0]
        number_values = j[1]
        for knk, k in enumerate(number_values):
            b[ini][1][jnj][1][knk] = k.average
