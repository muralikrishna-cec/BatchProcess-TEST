public class DecisionTree {
    public static void main(String[] args) {
        int x = 10;

        if (x > 0) {
            if (x < 100) {
                System.out.println("x is a positive number less than 100");
            } else {
                System.out.println("x is very large");
            }
        } else {
            System.out.println("x is not positive");
        }
    }
}
