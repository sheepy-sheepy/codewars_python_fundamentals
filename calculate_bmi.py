def bmi(weight, height):
    body_index = weight / height ** 2

    if body_index <= 18.5:
        return "Underweight"
    elif body_index <= 25:
        return "Normal"
    elif body_index <= 30:
        return "Overweight"
    return "Obese"
