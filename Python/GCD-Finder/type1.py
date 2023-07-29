# WAP in python to find the GCD of 2 numbers using the devision method.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

while b:
    a, b = b, a % b

print(f"The GCD of {a} and {b} is: {a}")