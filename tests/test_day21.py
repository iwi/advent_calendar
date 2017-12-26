import pytest
import day_20171221 as to


def test_get_piece():
    pattern = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
               [10, 11, 12, 13, 14, 15, 16, 17, 18],
               [20, 21, 22, 23, 24, 25, 26, 27, 28],
               [30, 31, 32, 33, 34, 35, 36, 37, 38],
               [40, 41, 42, 43, 44, 45, 46, 47, 48],
               [50, 51, 52, 53, 54, 55, 56, 57, 58],
               [60, 61, 62, 63, 64, 65, 66, 67, 68],
               [70, 71, 72, 73, 74, 75, 76, 77, 78],
               [80, 81, 82, 83, 84, 85, 86, 87, 88]]
    piece = [[3, 4, 5],
             [13, 14, 15],
             [23, 24, 25]]
    n_rows = 0
    m_cols = 1
    side = 3
    assert to.get_piece(n_rows, m_cols, side, pattern) == piece

    piece = [[66, 67, 68],
             [76, 77, 78],
             [86, 87, 88]]
    n = 2
    m = 2
    side = 3
    assert to.get_piece(n, m, side, pattern) == piece

def test_splitter():
    pattern = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
               [10, 11, 12, 13, 14, 15, 16, 17, 18],
               [20, 21, 22, 23, 24, 25, 26, 27, 28],
               [30, 31, 32, 33, 34, 35, 36, 37, 38],
               [40, 41, 42, 43, 44, 45, 46, 47, 48],
               [50, 51, 52, 53, 54, 55, 56, 57, 58],
               [60, 61, 62, 63, 64, 65, 66, 67, 68],
               [70, 71, 72, 73, 74, 75, 76, 77, 78],
               [80, 81, 82, 83, 84, 85, 86, 87, 88]]
    size = 9
    piece_side = 3
    pieces = [[[[0, 1, 2],
                [10, 11, 12],
                [20, 21, 22]],
               [[3, 4, 5],
                [13, 14, 15],
                [23, 24, 25]],
               [[6, 7, 8],
                [16, 17, 18],
                [26, 27, 28]]],
              [[[30, 31, 32],
                [40, 41, 42],
                [50, 51, 52]],
               [[33, 34, 35],
                [43, 44, 45],
                [53, 54, 55]],
               [[36, 37, 38],
                [46, 47, 48],
                [56, 57, 58]]],
              [[[60, 61, 62],
                [70, 71, 72],
                [80, 81, 82]],
               [[63, 64, 65],
                [73, 74, 75],
                [83, 84, 85]],
               [[66, 67, 68],
                [76, 77, 78],
                [86, 87, 88]]]]
    assert to.splitter(size, piece_side , pattern) == pieces 


def test_attach():
    pattern = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
               [10, 11, 12, 13, 14, 15, 16, 17, 18],
               [20, 21, 22, 23, 24, 25, 26, 27, 28],
               [30, 31, 32, 33, 34, 35, 36, 37, 38],
               [40, 41, 42, 43, 44, 45, 46, 47, 48],
               [50, 51, 52, 53, 54, 55, 56, 57, 58],
               [60, 61, 62, 63, 64, 65, 66, 67, 68],
               [70, 71, 72, 73, 74, 75, 76, 77, 78],
               [80, 81, 82, 83, 84, 85, 86, 87, 88]]
    pieces = [[[[0, 1, 2],
                [10, 11, 12],
                [20, 21, 22]],
               [[3, 4, 5],
                [13, 14, 15],
                [23, 24, 25]],
               [[6, 7, 8],
                [16, 17, 18],
                [26, 27, 28]]],
              [[[30, 31, 32],
                [40, 41, 42],
                [50, 51, 52]],
               [[33, 34, 35],
                [43, 44, 45],
                [53, 54, 55]],
               [[36, 37, 38],
                [46, 47, 48],
                [56, 57, 58]]],
              [[[60, 61, 62],
                [70, 71, 72],
                [80, 81, 82]],
               [[63, 64, 65],
                [73, 74, 75],
                [83, 84, 85]],
               [[66, 67, 68],
                [76, 77, 78],
                [86, 87, 88]]]]
    assert to.attach(pieces) == pattern


def test_split_pattern():
    pattern = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
               [10, 11, 12, 13, 14, 15, 16, 17, 18],
               [20, 21, 22, 23, 24, 25, 26, 27, 28],
               [30, 31, 32, 33, 34, 35, 36, 37, 38],
               [40, 41, 42, 43, 44, 45, 46, 47, 48],
               [50, 51, 52, 53, 54, 55, 56, 57, 58],
               [60, 61, 62, 63, 64, 65, 66, 67, 68],
               [70, 71, 72, 73, 74, 75, 76, 77, 78],
               [80, 81, 82, 83, 84, 85, 86, 87, 88]]
    pieces = [[[[ 0,  1,  2],
                [10, 11, 12],
                [20, 21, 22]],
               [[3, 4, 5],
                [13, 14, 15],
                [23, 24, 25]],
               [[6, 7, 8],
                [16, 17, 18],
                [26, 27, 28]]],
              [[[30, 31, 32],
                [40, 41, 42],
                [50, 51, 52]],
               [[33, 34, 35],
                [43, 44, 45],
                [53, 54, 55]],
               [[36, 37, 38],
                [46, 47, 48],
                [56, 57, 58]]],
              [[[60, 61, 62],
                [70, 71, 72],
                [80, 81, 82]],
               [[63, 64, 65],
                [73, 74, 75],
                [83, 84, 85]],
               [[66, 67, 68],
                [76, 77, 78],
                [86, 87, 88]]]]
    assert to.split_pattern(pattern) == pieces 

def test_split_pattern():
    pattern = [[0, 1, 2, 3, 4, 5, 6, 7, 8],
               [10, 11, 12, 13, 14, 15, 16, 17, 18],
               [20, 21, 22, 23, 24, 25, 26, 27, 28],
               [30, 31, 32, 33, 34, 35, 36, 37, 38],
               [40, 41, 42, 43, 44, 45, 46, 47, 48],
               [50, 51, 52, 53, 54, 55, 56, 57, 58],
               [60, 61, 62, 63, 64, 65, 66, 67, 68],
               [70, 71, 72, 73, 74, 75, 76, 77, 78],
               [80, 81, 82, 83, 84, 85, 86, 87, 88]]
    pieces = [[[[ 0,  1,  2],
                [10, 11, 12],
                [20, 21, 22]],
               [[3, 4, 5],
                [13, 14, 15],
                [23, 24, 25]],
               [[6, 7, 8],
                [16, 17, 18],
                [26, 27, 28]]],
              [[[30, 31, 32],
                [40, 41, 42],
                [50, 51, 52]],
               [[33, 34, 35],
                [43, 44, 45],
                [53, 54, 55]],
               [[36, 37, 38],
                [46, 47, 48],
                [56, 57, 58]]],
              [[[60, 61, 62],
                [70, 71, 72],
                [80, 81, 82]],
               [[63, 64, 65],
                [73, 74, 75],
                [83, 84, 85]],
               [[66, 67, 68],
                [76, 77, 78],
                [86, 87, 88]]]]
    assert to.split_pattern(pattern) == pieces 

    pattern = [[0, 1, 2, 3, 4, 5, 6, 7],
               [10, 11, 12, 13, 14, 15, 16, 17],
               [20, 21, 22, 23, 24, 25, 26, 27],
               [30, 31, 32, 33, 34, 35, 36, 37],
               [40, 41, 42, 43, 44, 45, 46, 47],
               [50, 51, 52, 53, 54, 55, 56, 57],
               [60, 61, 62, 63, 64, 65, 66, 67],
               [70, 71, 72, 73, 74, 75, 76, 77]]
    pieces = [[[[0, 1], [10, 11]],
               [[2, 3], [12, 13]],
               [[4, 5], [14, 15]],
               [[6, 7], [16, 17]]],
              [[[20, 21], [30, 31]],
               [[22, 23], [32, 33]],
               [[24, 25], [34, 35]],
               [[26, 27], [36, 37]]],
              [[[40, 41], [50, 51]],
               [[42, 43], [52, 53]],
               [[44, 45], [54, 55]],
               [[46, 47], [56, 57]]],
              [[[60, 61], [70, 71]],
               [[62, 63], [72, 73]],
               [[64, 65], [74, 75]],
               [[66, 67], [76, 77]]]]
    assert to.split_pattern(pattern) == pieces


def test_get_transforms():
    piece =   [[ 0,  1,  2],
               [10, 11, 12],
               [20, 21, 22]]
    rot_90 =  [[20, 10,  0],
               [21, 11,  1],
               [22, 12,  2]]
    rot_180 = [[22, 21, 20],
               [12, 11, 10],
               [ 2,  1,  0]]
    rot_270 = [[ 2, 12, 22],
               [ 1, 11, 21],
               [ 0, 10, 20]]
    flip_v =  [[20, 21, 22],
               [10, 11, 12],
               [ 0,  1,  2]]
    fv_rot_90 =  [[ 0, 10, 20],
                  [ 1, 11, 21],
                  [ 2, 12, 22]]
    fv_rot_180 = [[ 2,  1,  0],
                  [12, 11, 10],
                  [22, 21, 20]]
    fv_rot_270 = [[22, 12,  2],
                  [21, 11,  1],
                  [20, 10,  0]]
    flip_h =  [[ 2,  1,  0],
               [12, 11, 10],
               [22, 21, 20]]
    fh_rot_90 =  [[22, 12,  2],
                  [21, 11,  1],
                  [20, 10,  0]]
    fh_rot_180 = [[20, 21, 22],
                  [10, 11, 12],
                  [ 0,  1,  2]]
    fh_rot_270 = [[ 0, 10, 20],
                  [ 1, 11, 21],
                  [ 2, 12, 22]]
    assert to.get_transforms(piece) == [piece, flip_v, flip_h, rot_90, rot_180, rot_270,
                                        fv_rot_90, fv_rot_180, fv_rot_270, fh_rot_90,
                                        fh_rot_180, fh_rot_270]


def test_find_canonincal():
    piece = [[1, 0, 0],
             [1, 0, 1],
             [0, 1, 0]]
    lines = []
    with open('data/input_data_20171221.txt', 'r') as f:
        for line in f:
            lines.append(line.rstrip('\n'))
    rules = [to.parse_line(line) for line in lines]
    canonical= [[0, 1, 0],
                [1, 0, 1],
                [1, 0, 0]]
    assert to.find_canonical(piece, rules) == canonical

    piece = [[1, 1, 0],
             [0, 0, 1],
             [0, 1, 0]]
    canonical= [[0, 1, 0],
                [1, 0, 1],
                [1, 0, 0]]
    assert to.find_canonical(piece, rules) == canonical


def test_transform():
    canonical= [[0, 1, 0],
                [1, 0, 1],
                [1, 0, 0]]

    lines = []
    with open('data/input_data_20171221.txt', 'r') as f:
        for line in f:
            lines.append(line.rstrip('\n'))
    rules = [to.parse_line(line) for line in lines]

    transformed = [[1, 0, 0, 0],
                   [0, 1, 1, 1],
                   [0, 0, 0, 1],
                   [0, 0, 1, 0]]

    assert to.transform(canonical, rules) == transformed


def test_convert_all():
    pieces = [[[[0, 1, 0],
                [1, 0, 1],
                [1, 0, 0]],
               [[0, 1, 0],
                [1, 0, 1],
                [1, 0, 0]],
               [[0, 1, 0],
                [1, 0, 1],
                [1, 0, 0]]],
              [[[0, 1, 0],
                [1, 0, 1],
                [1, 0, 0]],
               [[0, 1, 0],
                [1, 0, 1],
                [1, 0, 0]],
               [[0, 1, 0],
                [1, 0, 1],
                [1, 0, 0]]],
              [[[0, 1, 0],
                [1, 0, 1],
                [1, 0, 0]],
               [[0, 1, 0],
                [1, 0, 1],
                [1, 0, 0]],
               [[0, 1, 0],
                [1, 0, 1],
                [1, 0, 0]]]]

    lines = []
    with open('data/input_data_20171221.txt', 'r') as f:
        for line in f:
            lines.append(line.rstrip('\n'))
    rules = [to.parse_line(line) for line in lines]

    transformed = [[[[1, 0, 0, 0],
                     [0, 1, 1, 1],
                     [0, 0, 0, 1],
                     [0, 0, 1, 0]],
                    [[1, 0, 0, 0],
                     [0, 1, 1, 1],
                     [0, 0, 0, 1],
                     [0, 0, 1, 0]],
                    [[1, 0, 0, 0],
                     [0, 1, 1, 1],
                     [0, 0, 0, 1],
                     [0, 0, 1, 0]]],
                   [[[1, 0, 0, 0],
                     [0, 1, 1, 1],
                     [0, 0, 0, 1],
                     [0, 0, 1, 0]],
                    [[1, 0, 0, 0],
                     [0, 1, 1, 1],
                     [0, 0, 0, 1],
                     [0, 0, 1, 0]],
                    [[1, 0, 0, 0],
                     [0, 1, 1, 1],
                     [0, 0, 0, 1],
                     [0, 0, 1, 0]]],
                   [[[1, 0, 0, 0],
                     [0, 1, 1, 1],
                     [0, 0, 0, 1],
                     [0, 0, 1, 0]],
                    [[1, 0, 0, 0],
                     [0, 1, 1, 1],
                     [0, 0, 0, 1],
                     [0, 0, 1, 0]],
                    [[1, 0, 0, 0],
                     [0, 1, 1, 1],
                     [0, 0, 0, 1],
                     [0, 0, 1, 0]]]]

    assert to.convert_all(pieces, rules) == transformed