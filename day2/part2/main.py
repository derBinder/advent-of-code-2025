def is_invalid_id(num):
    s = str(num)
    length = len(s)
    
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            repetitions = length // pattern_len
            
            if repetitions >= 2 and pattern * repetitions == s:
                return True
    
    return False

file = open('../input.in').read()
id_ranges = file.split(',')

if __name__ == '__main__':
    sum_id = 0

    for id_range in id_ranges:
        start, end = id_range.split('-')
        for i in range(int(start), int(end) + 1):
            if is_invalid_id(i):
                sum_id += i

    print(sum_id)
