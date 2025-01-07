def find_slope(points):
    x1, y1, x2, y2 = points # uppacking points, can't be the other way around
    if x1 == x2:
        return "undefined"
    else:
        slope = (y2 - y1) // (x2 - x1) # integer division
        return str((slope))
