def get_plate(weight):
    # increments = [2.5, 5, 10, 25, 35, 45]
    if weight < 2.5:
        return 0
    if 2.5 <= weight < 5:
        return 2.5
    if 5 <= weight < 10:
        return 5
    if 10 <= weight < 25:
        return 10
    if 25 <= weight < 35:
        return 25
    if 35 <= weight < 45:
        return 35
    if weight >= 45:
        return 45


def get_plates(w):
    w = (w - 45) / 2
    plates = []
    while (w != 0):
        ret = get_plate(w)
        plates.append(ret)
        w = w - ret
        # print(ret, w)
    print(plates)


if __name__ == "__main__":
    get_plates(135)