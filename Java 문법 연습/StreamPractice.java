import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class StreamPractice {
    public static void main(String[] args) {
        // List Stream------------------------------------------
        List<Integer> list1 = Arrays.asList(1,2,3,4,5);
        list1 = list1.stream().map(num -> num + 1).collect(Collectors.toList());
        list1.forEach(System.out::println);

    }
}
