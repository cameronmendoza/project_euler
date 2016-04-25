import sys

# remove raw_input weirdness
sys.stdout.flush()


def is_prime(num):
    # make sure num is a positive integer
    num = abs(int(num))

    if num < 2:
        return False

    # 2 is only even prime number
    if num == 2:
        return True
    # all other even numbers not prime
    if not num & 1:
        return False

    for x in range(3, int(num ** 0.5) + 1, 2):
        if num % x == 0:
            return False
    return True


def get_pfs(num):
    list_of_pfs = []
    for x in range(2, int(num ** 0.5) + 1):
        if is_prime(x) and (num % x == 0):
            list_of_pfs.append(x)
    return list_of_pfs


number = int(
    raw_input('Enter number to determine its largest prime factor: ')
            )

largest_prime_factor = max(get_pfs(number))

print 'Largest prime factor of %d is %d' % (number,
                                            largest_prime_factor)
