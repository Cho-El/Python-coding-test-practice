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
        String[] strArray1 = new String[5]; // null String은 객체이기에
        String[] strArray2 = {"a","b","c","d","e"};
        String[] strArray3 = new String[] {"a","b","c","d","e"};
        System.out.println("strArray1 : " + strArray1);
        System.out.println("strArray1 : " + Arrays.toString(strArray1));
        System.out.println("strArray2 : " + strArray2);
        System.out.println("strArray2 : " + Arrays.toString(strArray2));
        System.out.println("strArray3 : " + strArray3);
        System.out.println("strArray3 : " + Arrays.toString(strArray3));

        // int 초기화
        int[] intArray1 = new int[5]; // 초기값 0
        int[] intArray2 = {1,2,3,4,5};
        int[] intArray3 = new int[] {1,2,3,4,5};
        System.out.println("intArray1 : " + intArray1);
        System.out.println("intArray1 : " + Arrays.toString(intArray1));
        System.out.println("intArray2 : " + intArray2);
        System.out.println("intArray2 : " + Arrays.toString(intArray2));
        System.out.println("intArray3 : " + intArray3);
        System.out.println("intArray3 : " + Arrays.toString(intArray3));


        //Set-----------------------------------------------
        Set<Integer> setInteger = new HashSet<>(Arrays.asList(1,2,3));
        Set<String> setString = new HashSet<>(Arrays.asList("a","b"));
        
        //데이터 삽입
        setInteger.add(4);
        setInteger.add(1);
        setString.add("c");
        setString.add("a");
        setString.remove("c");

        System.out.println("setInteger : " + setInteger);
        System.out.println("setString : " + setString);

        // ArrayList----------------------------------------
        // 초기화
        List<Integer> arrayList1 = new ArrayList<>();
        List<Integer> arrayList2 = new ArrayList<>(Arrays.asList(1,2,3,4,5));
        List<Integer> arrayList3 = new ArrayList<>(setInteger);

        // 데이터 삽입
        arrayList1.add(2);
        arrayList1.add(3);
        arrayList1.add(1);

        // 데이터 삭제
        System.out.println("removing index 0 return result : " + arrayList1.remove(0));// int형을 전달 시 index로 취급된다. 해당 값 2 반환
        System.out.println("removing value 2 return result : " + arrayList1.remove(Integer.valueOf(2))); // false 반환
        System.out.println("arrayList1 : " + arrayList1);
        System.out.println("removing index 1 return result : " + arrayList1.remove(0));
        System.out.println("arrayList1[0] : " + arrayList1.get(0));
        System.out.println("arrayList1 : " + arrayList1);
        System.out.println("arrayList2 : " + arrayList2);
        System.out.println("arrayList3 : " + arrayList3);
    }
}
