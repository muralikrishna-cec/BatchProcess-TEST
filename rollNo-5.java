public class CalculatorApp {

    public static int add(int a, int b) {
        return a + b;
    }

    public static int multiply(int a, int b) {
        return a * b;
    }

    public static void printResults(int a, int b) {
        System.out.println("Sum: " + add(a, b));
        System.out.println("Product: " + multiply(a, b));
    }

    public static void main(String[] args) {
        int x = 5;
        int y = 3;

        if (x > y) {
            printResults(x, y);
        } else {
            System.out.println("x is not greater than y");
        }

        for (int i = 0; i < 2; i++) {
            System.out.println("i: " + i);
        }
    }
}
