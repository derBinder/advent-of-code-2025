file = open('../input.in').read()
rows = file.split('\n')

if __name__ == '__main__':
    zero_count = 0
    position = 50

    for row in rows:
        direction = row[0]
        steps = int(row[1:])

        if direction == 'L':
            position = (position - steps) % 100
        else:
            position = (position + steps) % 100

        if position == 0:
            zero_count += 1

    print(zero_count)
