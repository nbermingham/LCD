l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

def isPrime(n):
    """ Checks to see if n is prime
    """

    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 6
    while i * i <= n:
        if n % (i + 1) == 0 or n % (i - 1) == 0:
            return False
        i += 6
    
    return True


def prime_fact(n):
    """return the prime factorization of number n in dict form
    """
    if n == 1:
        return {}
    d = {}
    while n > 1:
        for i in range(2, n+1):
            if i == 1:
                continue
            if n%i == 0 and isPrime(i):
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
                break
        n //= i
    
    return d

print(prime_fact(15))

def lcd(l):
    """returns the least common divisor of a list of integers using prime factorization
    """
    if len(l) == 1:
        return l[0]
    
    max_primes = prime_fact(l[0])
    for i in range(len(l)):
        new_primes = prime_fact(l[i])
        for key in new_primes.keys():
            if key not in max_primes:
                max_primes[key] = new_primes[key]
            else:
                max_primes[key] = max(max_primes[key], new_primes[key])
    
    lcd = 1
    for key in max_primes.keys():
        lcd *= key**max_primes[key]
    
    return lcd

print(lcd(l))


def brute_lcd(l):
    """brute force method to determine the least common divisor of a list l
    """
    num = max(l)
    works = False

    while not works:
        for i in range(len(l)):
            if num % l[i] != 0:
                break
            else:
                if i == len(l) - 1:
                    works = True
                else:
                    continue
        
        if works:
            return(num)
        else:
            num += 1

print(brute_lcd(l))



