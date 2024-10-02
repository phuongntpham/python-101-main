# Print out every prime number between 1 and 1000.
for number in range(1, 1001):
    if number < 2:
        pass
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print(number)