def check(num):
    if num > 0:
        return "Positive"
    else:
        return "Non-positive"


if __name__ == "__main__":
    print("Check(5):", check(5))
    print("Check(-2):", check(-2))
