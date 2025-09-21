import java.util.*;

public class StudentManager {

    static class Student {
        String name;
        int marks;

        Student(String name, int marks) {
            this.name = name;
            this.marks = marks;
        }

        boolean isPassed() {
            return marks >= 40;
        }
    }

    public static void printTopper(List<Student> students) {
        Student topper = null;
        for (Student s : students) {
            if (topper == null || s.marks > topper.marks) {
                topper = s;
            }
        }
        if (topper != null) {
            System.out.println("Topper: " + topper.name + " (" + topper.marks + ")");
        }
    }

    public static void printPassFail(List<Student> students) {
        for (Student s : students) {
            if (s.isPassed()) {
                System.out.println(s.name + ": Passed");
            } else {
                System.out.println(s.name + ": Failed");
            }
        }
    }

    public static void main(String[] args) {
        List<Student> students = new ArrayList<>();
        students.add(new Student("Alice", 85));
        students.add(new Student("Bob", 32));
        students.add(new Student("Charlie", 55));
        students.add(new Student("David", 73));

        printTopper(students);
        printPassFail(students);
    }
}
