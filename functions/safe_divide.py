def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Done")
    return result


if __name__ == "__main__":
    print("Safe Divide:", safe_divide(10, 0))
    print("Safe Divide:", safe_divide(10, 2))
