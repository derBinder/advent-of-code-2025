file = open('../input.in').read()
rows = file.split('\n')

if __name__ == '__main__':
    total_joltage = 0

    for bank in rows:
        joltage = bank[0] + bank[1]

        for idx, first in enumerate(bank):
            for second in bank[idx + 1:]:
                temp_joltage = first + second
                if int(temp_joltage) > int(joltage):
                    joltage = temp_joltage

        total_joltage += int(joltage)

    print(total_joltage)
