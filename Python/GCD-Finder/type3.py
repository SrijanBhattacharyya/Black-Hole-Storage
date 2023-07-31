# WAP in python to find the GCD of n numbers using PRIME FACTORISATION method.
def fact (num: int) -> list:
    factors = []
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            factors.append (i)
    if num > 1:
        factors.append (num)
    return factors

def gcd_n (numbers: list) -> int:
    fact_list = [fact (num) for num in numbers]

    common_factors = {}
    for factors in fact_list:
        for factor in set (factors):
            if factor in common_factors:
                common_factors [factor] = min (common_factors[factor], factors.count (factor))
            else:
                common_factors [factor] = factors.count (factor)

    gcd = 1
    for factor, count in common_factors.items ():
        gcd *= factor ** count

    return gcd

def main () -> None:
    try:
        n = int (input ("Enter the number of elements: "))
        numbers = []
        for i in range (n):
            num = int (input ("    Enter a number: "))
            numbers.append (num)

        print (f"The GCD of {numbers} is {gcd_n (numbers)}")

    except ValueError:
        print ("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main ()
