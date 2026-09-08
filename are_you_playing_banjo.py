def are_you_playing_banjo(name: str):
    is_start_r = "plays" if name.startswith(("r", "R")) else "does not play"
    return f"{name} {is_start_r} banjo"


print(are_you_playing_banjo("bravo"))
