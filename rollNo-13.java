public class TrickyLoops {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        int sum = 0;

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if ((i + j) % 2 == 0) {
                    sum += matrix[i][j];
                    System.out.println("Adding " + matrix[i][j] + " at position [" + i + "][" + j + "]");
                } else {
                    sum -= matrix[i][j];
                    System.out.println("Subtracting " + matrix[i][j] + " at position [" + i + "][" + j + "]");
                }
            }
        }

        System.out.println("Final Sum: " + sum);

        // Additional tricky loop
        int factorial = 1;
        for (int k = 1; k <= 5; k++) {
            factorial *= k;
            if (factorial % 2 == 0) {
                factorial /= 2;
            }
            System.out.println("Step " + k + ": factorial = " + factorial);
        }
    }
}
