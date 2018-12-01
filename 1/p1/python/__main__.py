print(
    sum(
        [
            int(number) for number in
            map(int, open('input.txt').read().strip().split('\n'))
        ]
    )
)
