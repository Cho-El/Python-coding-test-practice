import java.util.Arrays;

public class PracticeJava {
    public static void main(String[] args) {
        // Comparable과 Comparator
        // 정렬 -------
        Student[] studentArray = new Student[2];
        studentArray[0] = new Student(10,18);
        studentArray[1] = new Student(5,20);

        for (Student s : studentArray) {
            System.out.println("age : " + s.age);
        }
        Arrays.sort(studentArray);
        for (Student s : studentArray) {
            System.out.println("age : " + s.age);
        }
    }

    public static class Student implements Comparable<Student> {
        int age;
        int classNumber;

        public Student(int age, int classNumber) {
            this.age = age;
            this.classNumber = classNumber;
        }
        @Override
        public int compareTo(Student o) {
            return Integer.compare(this.age, o.age);
        }
    }
}


