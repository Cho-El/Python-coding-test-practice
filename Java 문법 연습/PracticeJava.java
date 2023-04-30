import java.util.Arrays;

public class PracticeJava {
    private static int globalClassVar = 0; // 전역 변수이자 클래스 변수
    private int globalInstanceVar = 0;
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

    public void nonStaticMethod() {
        globalClassVar++;
        globalInstanceVar++;
        /*
            전역 변수 static 여부와 상관없이 접근 가능
         */
        System.out.println(globalClassVar);
    }

    public static void staticMethod() {
        globalClassVar++;
        // globalInstanceVar++; 인스턴스 변수의 경우 접근 불가 
    }
}


