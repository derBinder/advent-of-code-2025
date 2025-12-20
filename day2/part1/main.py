file = open('../input.in').read()
id_ranges = file.split(',')

if __name__ == '__main__':
    sum_id = 0

    for id_range in id_ranges:
        start, end = id_range.split('-')
        for i in range(int(start), int(end) + 1):
            if len(str(i)) % 2 == 0:
                first_half = str(i)[:len(str(i))//2]
                second_half = str(i)[len(str(i))//2:]

                if first_half == second_half:
                    sum_id += i

    print(sum_id)
