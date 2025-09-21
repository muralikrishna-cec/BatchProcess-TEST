def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    print("GCD(48, 18):", gcd(48, 18))
