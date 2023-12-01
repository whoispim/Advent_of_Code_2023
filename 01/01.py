import re


def part_a():
    result = 0

    with open('01/input.txt', 'r') as f:
        for line in f.readlines():
            first = re.search('^\D*(\d)', line).group(1)
            last = re.search('(\d)\D*$', line).group(1)
            result += int(first + last)

    print(f'a: The result of adding up all calibration values hidden in the input is {result}.')


def part_b():
    result = 0
    numdict = {
        ['one','two','three','four','five','six','seven','eight','nine'][x]: str(x+1)
        for x in  range(9)
    }

    with open('01/input.txt', 'r') as f:
        for line in f.readlines():
            first = re.search('^\D*?(\d|one|two|three|four|five|six|seven|eight|nine)', line).group(1)
            # Ti esrever dna ti pilf nwod gnaht ym tup i
            last  = re.search('^\D*?(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)', line[::-1]).group(1)[::-1]
            if first in numdict:
                first = numdict[first]
            if last in numdict:
                last = numdict[last]
            result += int(first + last)

    print(f'b: The result of adding up ALL calibration values hidden in the input is {result}.')


if __name__ == '__main__':
    part_a()
    part_b()
