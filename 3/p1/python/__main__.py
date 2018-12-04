import re


MATRIX_SIZE = 1000, 1000


def get_empty_matrix(width, height):
    return [[0 for i in range(width)] for i in range(height)]


def get_point(line):
    d = list(map(int, re.findall('\d+', line)))

    return {'id': d[0], 'x': d[1], 'y': d[2], 'w': d[3], 'h': d[4]}


def get_points():
    return [get_point(line) for line in open('input.txt').readlines()]


def get_inches_of_fabric(matrix, points):
    for point in points:
        for x in range(point['x'], point['x']+point['w']):
            for y in range(point['y'], point['y']+point['h']):
                matrix[x][y] += 1

    return sum([len(row) - row.count(0) - row.count(1) for row in matrix])


if __name__ == '__main__':
    matrix = matrix = get_empty_matrix(*MATRIX_SIZE)
    print(get_inches_of_fabric(matrix, get_points()))
