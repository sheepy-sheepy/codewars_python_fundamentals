def spin_words(string: str):
    return " ".join(word[::-1] if len(word) >= 5 else word
                    for word in string.split())


print(spin_words("Hey fellow warriors"))
