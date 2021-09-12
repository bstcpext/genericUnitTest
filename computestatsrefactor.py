file = 'random_nums'


def read_ints():
    data = []
    with open(file, 'r') as f:
        for line in f:
            num = int(line)
            data.append(num)
        return data


def count():
    data = read_ints()
    i = 0
    while i < len(data):
        i =+ 1
    return i


def summation():
    sum = 0
    data = read_ints()
    for x in data:
        sum += x
    return sum


def average():
    return summation() / count()


def standard_deviation():
    pass


if __name__ == '__main__':
    print(read_ints())
    print(count())
    print(summation())
    print(average())

"""
harmonic_mean: Returns the harmonic mean of the elements in random_nums.txt

variance: Returns the variance of the elements in random_nums.txt 

standard_dev: Returns the standard deviation of all of the elements in random_nums.txt
"""