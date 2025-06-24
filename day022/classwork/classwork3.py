def capitalize_names(names):
    new_names = []
    for name in names:
        big = name.upper()
        new_names.append(big)
    return new_names


print(capitalize_names(["giorgi", "nino", "luka"]))
