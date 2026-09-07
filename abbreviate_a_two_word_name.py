def abbrev_name(name: str):
    name_list = [name_path[0] for name_path in name.title().split()]
    return ".".join(name_list)


print(abbrev_name("Sam Harris"))  # S.H
print(abbrev_name("patrick feenan"))  # P.F
print(abbrev_name("Evan C"))  # E.C
