import random
#var = 4? 

def IsPrimeNumber(N):
    if N < 2:
        return False #Натуральное число, большее 1 , называется простым, если оно ни на что не делится, кроме себя и 1
    max_div = int(N**0.5) + 1
    for i in range(2, max_div):
        if N % i == 0:
            return False
    return True



random_numbers = [random.randint(1, 1000) for _ in range(5)]
for num in random_numbers:
    result = IsPrimeNumber(num)
    print(f"Число {num} {'простое' if result else 'не простое'}")