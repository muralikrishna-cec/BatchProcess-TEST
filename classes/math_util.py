class MathUtils:
    def factorial(self, n):
        if n <= 1:
            return 1
        return n * self.factorial(n - 1)

    def fibonacci(self, n):
        if n <= 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)


if __name__ == "__main__":
    math = MathUtils()
    print("Factorial(5):", math.factorial(5))
    print("Fibonacci(6):", math.fibonacci(6))
