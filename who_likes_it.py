def likes(names: list[str]) -> str:
    length_names = len(names)
    end = "like this" if length_names > 1 else "likes this"

    if length_names:
        if length_names > 1:
            if length_names > 2:
                if length_names > 3:
                    return f"{', '.join(names[:2])} and {length_names - 2} others {end}"
                return f"{', '.join(names[:2])} and {names[2]} {end}"
            return f"{' and '.join(names[:2])} {end}"
        return f"{names[0]} {end}"
    return f"no one {end}"
