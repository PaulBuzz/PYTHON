print("Let's check if the number is prime or not.")

def prime_checker(number):
    is_prime = True
    for i in range(2, 100):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Number is prime.")
    else:
        print("Number is not prime.")


n = int(input("Check this number: "))
prime_checker(number=n)
