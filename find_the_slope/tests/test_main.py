from source.main import find_slope


def test_same_x_coords():
    # arrange
    x1, y1, x2, y2 = 1, 2, 1, 3
    # act
    result = find_slope(x1, y1, x2, y2)
    # assert
    assert result == "undefined"

def test_same_y_coords():
    # arrange
    x1, y1, x2, y2 = 1, 2, 4, 2
    # act
    result = find_slope(x1, y1, x2, y2)
    # assert
    assert result == 0

