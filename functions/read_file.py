def read_file(path):
    with open(path, "r") as f:
        return f.read()


if __name__ == "__main__":
    # create a test file
    with open("sample.txt", "w") as f:
        f.write("Hello File!")
    print("Read File:", read_file("sample.txt"))
