# Prime numbers

# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    if number > 2:
        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
                break

    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

primes = [53, 157, 173, 211, 257, 263, 373, 563, 593, 607, 653, 733,
          947, 977, 1103, 1123, 1187, 1223, 1367, 1511, 1747, 1753,
          1907, 2287, 2417, 2677, 2903, 2963, 3307, 3313, 3637, 3733,
          4013, 4409, 4457, 4597, 4657, 4691, 4993, 5107, 5113, 5303,
          5387, 5393, 27644437,
          35742549198872617291353508656626642567,
          359334085968622831041960188598043661065388726959079837]

print("\nChecking list of primes")
def prime_list_checker(list):
    p_count = 0
    for number in primes:
        if not number % 2 == 0 or not number % 3 == 0 or not number % 5 == 0:
            print("It's a prime number")
            p_count += 1
        else:
            print("It's not a prime number")
    print(f"Counted {p_count} primes.")

prime_list_checker(primes)

print(f"Primes in list: {len(primes)}")
