public class SimpleLoops {
    public static void main(String[] args) {
        int sum = 0;

        for (int i = 1; i <= 5; i++) {
            if (i % 2 == 0) {
                sum += i;
                System.out.println("Adding " + i);
            } else {
                sum -= i;
                System.out.println("Subtracting " + i);
            }
        }

        System.out.println("Final Sum: " + sum);

        // Another tricky loop
        int num = 1;
        for (int j = 1; j <= 5; j++) {
            num *= j;
            if (num % 3 == 0) {
                num /= 3;
            }
            System.out.println("Step " + j + ": num = " + num);
        }
    }
}
