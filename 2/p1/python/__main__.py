ids = open('input.txt').read().strip().split('\n')


def count_char(identifier, n):
    return sum([identifier.count(char) == n for char in identifier]) != 0


def get_checksum(ids):
    return sum([count_char(id, 2) for id in ids]) *\
        sum([count_char(id, 3) for id in ids])


print(get_checksum(ids))
