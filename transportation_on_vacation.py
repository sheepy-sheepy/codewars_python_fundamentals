def rental_car_cost(d):
    price = 40 * d
    if d >= 3:
        if d >= 7:
            return price - 50
        return price - 20
    return price
