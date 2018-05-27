def colors_match(color_1, color_2, allowed_difference):
    red_delta = abs(color_1[0] - color_2[0])
    green_delta = abs(color_1[1] - color_2[1])
    blue_delta = abs(color_1[2] - color_2[2])

    if red_delta <= allowed_difference and green_delta <= allowed_difference and blue_delta <= allowed_difference:
        return True

    return False