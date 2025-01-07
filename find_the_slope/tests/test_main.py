from source.main import find_slope


def test_same_x_coords():
    # arrange
    points = [1, 2, 1, 5]
    # act
    result = find_slope(points)
    # assert
    assert result == "undefined"

def test_same_y_coords():
    # arrange
    points = [19, 3, 20, 3]
    # act
    result = find_slope(points)
    # assert
    assert result == 0

def test_various_coords():
    # arrange
    points = [10, 50, 30, 150]
    # act
    result = find_slope(points)
    # assert
    assert result == 5

def test_another_from_fcc_test():
    # arrange
    points = [10, 20, 20, 80]
    # act
    result = find_slope(points)
    # assert
    assert result == 6
