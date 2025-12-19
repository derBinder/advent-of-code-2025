file = open('./input.in').read()
rows = file.split('\n')

def part1():
    zero_count = 0
    position = 50

    for row in rows:
        direction = row[0]
        steps = int(row[1:])

        for _ in range(steps):
            if direction == 'L':
                position = (position - 1) % 100
            else:
                position = (position + 1) % 100
            
            if position == 0:
                zero_count += 1

    return zero_count

if __name__ == '__main__':
    print('Part 1:', part1())
