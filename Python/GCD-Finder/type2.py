# WAP in python to find the GCD of n numbers.
def find_gcd (a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def find_gcd_of_n_numbers (numbers: list) -> int:
    result = numbers [0]
    for num in numbers [1:]:
        result = find_gcd (result, num)
    return result

def main () -> None:
    try:
        n = int (input ("Enter the number of elements: "))
        numbers = []
        for i in range (n):
            num = int (input (f"Enter number {i+1}: "))
            numbers.append (num)

        gcd = find_gcd_of_n_numbers(numbers)
        print(f"The GCD of {numbers} is {gcd}")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
