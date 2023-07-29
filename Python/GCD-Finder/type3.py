# WAP in python to find the GCD of n numbers using PRIME FACTORISATION method.
def prime_factors(num):
    factors = []
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append(i)
    if num > 1:
        factors.append(num)
    return factors

def find_gcd_of_n_numbers(numbers):
    prime_factors_list = [prime_factors(num) for num in numbers]

    common_factors = {}
    for factors in prime_factors_list:
        for factor in set(factors):
            if factor in common_factors:
                common_factors[factor] = min(common_factors[factor], factors.count(factor))
            else:
                common_factors[factor] = factors.count(factor)

    gcd = 1
    for factor, count in common_factors.items():
        gcd *= factor ** count

    return gcd

def main():
    try:
        n = int(input("Enter the number of elements: "))
        numbers = []
        for i in range(n):
            num = int(input(f"Enter number {i+1}: "))
            numbers.append(num)

        gcd = find_gcd_of_n_numbers(numbers)
        print(f"The GCD of {numbers} is {gcd}")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
