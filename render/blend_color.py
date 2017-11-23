def blend(rate, color, background):
    background_rate = 1 - rate

    return (
        color[0] * rate + background[0] * background_rate,
        color[1] * rate + background[1] * background_rate,
        color[2] * rate + background[2] * background_rate
    )
