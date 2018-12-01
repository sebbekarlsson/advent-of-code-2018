inputs = map(int, open('input.txt').read().strip().split('\n'))


loop = True
v = 0
seen = set()
while loop:
    for n in inputs:
        v += n
        if v in seen:
            print(v)
            loop = False
            break
        seen.add(v)
