def is_palindrome(s):
    return s == s[::-1]


if __name__ == "__main__":
    print("Palindrome 'racecar':", is_palindrome("racecar"))
    print("Palindrome 'hello':", is_palindrome("hello"))
