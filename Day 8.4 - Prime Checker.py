# Write your code below this line 👇
import math
def prime_checker(number):
    prime = True
    nSqr = math.isqrt(number)
    if number % 2 == 0 or number % 3 == 0:
        prime = False
    else:
        for n in range(4, nSqr):
            if number % n == 0:
                prime = False

    if prime:
        print("It\'s a prime number.")
    else:
        print("It\'s not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
