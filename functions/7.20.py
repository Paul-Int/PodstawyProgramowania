def f(n):
    count = 0
    num = 1

    while count < n:
        num += 1
        if num < 2:
            continue

        is_prime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            count += 1

    return num

print(f(1))
print(f(5))