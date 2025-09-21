def nested(a, b):
    for i in range(a):
        if i % 2 == 0:
            while b > 0:
                b -= 1
        else:
            pass
    return b


if __name__ == "__main__":
    print("Nested(3, 5):", nested(3, 5))
