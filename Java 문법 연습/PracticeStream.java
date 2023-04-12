import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import javax.sound.sampled.SourceDataLine;

public class PracticeStream {
    public static void main(String[] args) {
        // 자료형 연습 --------------------------------------
        // Array--------------------------------------------
        // String 초기화
        String[] strArray1 = new String[5];
        String[] strArray2 = {"a","b","c","d","e"};
        String[] strArray3 = new String[] {"a","b","c","d","e"};
        System.out.println("strArray1 : " + strArray1);
        System.out.println("strArray2 : " + strArray2);
        System.out.println("strArray3 : " + strArray3);

        // int 초기화
        int[] intArray1 = new int[5]; // 초기값 0
        int[] intArray2 = {1,2,3,4,5};
        int[] intArray3 = new int[] {1,2,3,4,5};
        System.out.println("intArray1 : " + intArray1);
        System.out.println("intArray2 : " + intArray2);
        System.out.println("intArray3 : " + intArray3);


        //Set-----------------------------------------------
        Set<Integer> setInteger = new HashSet<>(Arrays.asList(1,2,3));
        Set<String> setString = new HashSet<>(Arrays.asList("a","b"));
        setInteger.add(4);
        setInteger.add(1);
        setString.add("c");
        setString.add("a");
        System.out.println(setInteger);
        System.out.println(setString);

        // ArrayList----------------------------------------
        // 초기화
        List<Integer> arrayList1 = new ArrayList<>();
        List<Integer> arrayList2 = new ArrayList<>(Arrays.asList(1,2,3,4,5));
        arrayList1.add(2);
        arrayList1.add(3);
        System.out.println(arrayList1.get(0));
    }
}
