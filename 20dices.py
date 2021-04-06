from sympy  import FiniteSet
def probability(sample, event):
    return len(event)/len(sample)

def check_prime(number):
    if number != 1:
        for factor in range(2, number):
            if number % factor == 0:
                return False
    else:
        return False
    return True

if __name__ == '__main__':
    space = FiniteSet(*range(1,21))
    primes = []
    for num in space:
        if check_prime(num):
            primes.append(num)
    event = FiniteSet(*primes)
    p = probability(space, event)
    
    print('Sample Space {0}'.format(space))
    print('Event: {0}'.format(event))
    print('Probability of rolling a prime: {0:.5f}'.format(p))
