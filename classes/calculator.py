class Calculator:
    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        result = 0
        for _ in range(abs(y)):
            result += x
        return result if y >= 0 else -result

    def factorial(self, n):
        if n < 0:
            raise ValueError("Negative factorial not allowed")
        result = 1
        for i in range(1, n + 1):
            result = self.multiply(result, i)
        return result

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Division by zero")
        return x / y


if __name__ == "__main__":
    calc = Calculator()
    print("Add:", calc.add(3, 7))
    print("Multiply:", calc.multiply(4, -3))
    print("Factorial:", calc.factorial(6))
    print("Divide:", calc.divide(10, 2))
