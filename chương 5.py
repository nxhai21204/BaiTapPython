
so_gioi_han = 100
def so_nguyen_to(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
def cac_so_nguyen_to(gioi_han):
    primes = []

    for i in range(2, gioi_han + 1):
        if so_nguyen_to(i):
            primes.append(i)
            print(f"{i} là số nguyên tố ")



cac_so_nguyen_to(so_gioi_han)