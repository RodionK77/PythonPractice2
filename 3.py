def generate_groups(groups):
    full_groups = []
    for i in groups:
        for j in range(1, groups[i] + 1):
            full_groups.append(i + "-" + str(j) + "-20")
        full_groups.append(" ")
    [print(i) for i in full_groups]


gr = {"ИВБО": 13, "ИКБО": 30, "ИНБО": 15, "ИМБО": 2}
generate_groups(gr)
