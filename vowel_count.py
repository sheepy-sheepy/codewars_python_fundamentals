def get_count(string):
    return sum(char in "aeiou" for char in string)
