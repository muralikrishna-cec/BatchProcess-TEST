def process(data):
    result = []
    for d in data:
        if isinstance(d, int):
            result.append(d * 2)
        elif isinstance(d, str):
            try:
                num = int(d)
                result.append(num)
            except ValueError:
                continue
    return result


if __name__ == "__main__":
    print("Process:", process([1, "2", "abc", 3]))
