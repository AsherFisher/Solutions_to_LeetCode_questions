





Q 3

import operator


def is_point_in_ring(r, x, y, relate):
    return relate(pow(x, 2) + pow (y, 2), pow(r, 2))


def solution(inner, outer, points_x, points_y):
    points_number = 0

    for x, y in zip(points_x, points_y):
        if is_point_in_ring(inner, x, y, operator.le):
            continue

        if is_point_in_ring(outer, x, y, operator.lt):
            points_number += 1

    return points_number






if __name__ == "__main__":
    print(solution(2, 4, [4, 0, 1, -2], [-4, 4, 3, 0]))


    # print(solution(1, 3, [0,1,2,-2,3], [0,1,4,1,0]))
    # print(solution(".X..X"))
    # print(solution ([51,71,17,42]))
    # print(solution ([51,32,43]))