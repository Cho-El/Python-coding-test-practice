import java.util.*;
import java.util.stream.IntStream;

public class PracticeDataStructure {
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
        System.out.println("strArray3 length : " + strArray3.length);
        // String 배열 순회
        for (String str : strArray2) {
            System.out.println("strArray2 element : " + str);
        }
        Arrays.stream(strArray2).forEach(System.out::println);
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
        List<Integer> arrayList4 = new ArrayList<>() {{
            add(5);
            add(6);
            add(7);
        }};

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
        System.out.println("arrayList4 : " + arrayList4);
        System.out.println("arraList1 size : " + arrayList1.size());
        
        // 데이터 순회
        for (Integer arrayListE : arrayList4) { // for each 문
            System.out.print(arrayListE + " ");
        }
        System.out.println();
        for (int i = 0; i < arrayList4.size(); i++) {
            System.out.print(arrayList4.get(i) + " ");
        }
        System.out.println();
        arrayList4.forEach((element) -> {
            System.out.println("element : " + element);
        });
        arrayList4.stream().forEach((element) -> System.out.println("element : " + element));
        arrayList4.stream().forEach(System.out::println);

        // HashMap-------------------------------------------- 순서 없음
        // TreeMap(Key 정렬)과 LinkedHashMap(입력 순서)이 존재
        // 초기화 생성
        Map<String, Integer> hashMap1 = new HashMap<>();
        Map<String, Object> hashMap2 = new HashMap<>() {{
            put("name", "yoon");
            put("nickname", "cho-el");
        }}; // 이 방식을 많이 활용
        Map<String, Object> immutableMap = Map.of(
            "score", "32",
            "nickname", "june"
        ); // 개수가 10개까지 제한이 있다.
        Map<Integer, String> immutableMap2 = Map.ofEntries(
            Map.entry(1,"kim"),
            Map.entry(2, "cho"),
            Map.entry(3,"na")
        ); // 10 개 이상 초기화 가능
        System.out.println();
        System.out.println(immutableMap);

        // 데이터 삽입 및 수정
        hashMap1.put("a", 1);
        hashMap1.put("b", 2);
        hashMap1.put("c",3);
        
        hashMap2.put("email", "syzzang21c@naver.com");
        hashMap2.put("name", "Na");
        // immutableMap.put("score", "40"); Map.of로 생성한 인스턴스는 수정할 수 없다.
        
        // 데이터 순회
        for (Map.Entry<Integer,String> entry : immutableMap2.entrySet()) {
            System.out.println("key : " + entry.getKey() + " value : " + entry.getValue());
        }
        for (Integer key : immutableMap2.keySet()) {
            System.out.println("key : " + key + " value : " + immutableMap2.get(key));
        }
        immutableMap2.entrySet().forEach(
            (entry) -> {
                System.out.println("key : " + entry.getKey() + " value : " + entry.getValue());
            });

        // Stack ---------------------------------------------
        // 선언
        Stack<String> stringStack = new Stack<>();
        Stack<Integer> intgerStack = new Stack<>();

        stringStack.push("a");
        stringStack.push("b");
        stringStack.push("c");
        stringStack.push("d");
        stringStack.pop();
        stringStack.empty();
        System.out.println("stringStack : " + stringStack);
        System.out.println("stringStack.contains(\"a\") : " + stringStack.contains("a"));
        System.out.println("stringStackElement : " + stringStack);
        stringStack.stream().forEach(System.out::println);
        System.out.println("stringStack.peek() : " + stringStack.peek());
        System.out.println("a index : " + stringStack.search("a"));
        System.out.println("get 0 index : " + stringStack.get(0));

        // Q -------------------------------------------------
        Queue<String> stringQ = new LinkedList<String>(Arrays.asList("a","b","c"));
        Queue<Integer> integerQ = new LinkedList<>();
        integerQ.add(1);
        integerQ.add(2);
        integerQ.add(3);
        System.out.println("q first value : " + integerQ.poll());
        System.out.println("integerQ : " + integerQ);
        System.out.println("integerQ have 2 : " + integerQ.contains(2));
        System.out.println("integerQ.element : " + integerQ.element());
        System.out.println("integerQ.peek : " + integerQ.peek());

        // Deque 양방향 Q--------------------------------------
        Deque<Integer> dequeInteger = new ArrayDeque<>();
        dequeInteger.addFirst(1);
        dequeInteger.offerFirst(2);
        dequeInteger.addLast(3);
        dequeInteger.add(4);
        dequeInteger.offerLast(5);
        System.out.println("dequeInteger : " + dequeInteger);
        dequeInteger.removeFirst(); // 첫 번째 삭제
        System.out.println("removeFirst dequeInteger : " + dequeInteger);
        dequeInteger.poll(); // 첫 번째 삭제
        System.out.println("poll dequeInteger : " + dequeInteger);
        System.out.println("pollLast dequeInteger : " + dequeInteger.pollLast());
        System.out.println("removeLast dequeInteger : " + dequeInteger.removeLast());

        // 우선순위 Q-------------------------------------------
        PriorityQueue<Integer> priorityQueueLowest = new PriorityQueue<>();
        PriorityQueue<Integer> priorityQueueHighest = new PriorityQueue<>(Collections.reverseOrder());
        priorityQueueLowest.add(1);
        priorityQueueLowest.add(50);
        priorityQueueLowest.add(10);
        priorityQueueLowest.add(100);
        priorityQueueHighest.add(1);
        priorityQueueHighest.add(50);
        priorityQueueHighest.add(10);
        priorityQueueHighest.add(100);
        System.out.println(priorityQueueLowest.peek());
        System.out.println(priorityQueueLowest.poll());
        System.out.println(priorityQueueHighest.peek());
        System.out.println(priorityQueueHighest.poll());
        System.out.println(priorityQueueLowest.isEmpty());

        System.out.println("Integer.compare(1,2) : " + Integer.compare(1,2)); // -1
        System.out.println("Integer.compare(2,1) : " + Integer.compare(2,1)); // 1
        PriorityQueue<Integer[]> pq = new PriorityQueue<>((o1, o2) -> {
            // 만일 2차원 배열의 첫 번째 원소가 같다면, 2번째 원소를 기준으로 내림차순 정렬한다.
            if(o1[0].equals(o2[0])) {
                return Integer.compare(o2[1], o1[1]);
            }
            // 2차원 배열의 첫 번째 원소를 기준으로 오름차순 정렬한다.
            return Integer.compare(o1[0], o2[0]);
        });
        pq.offer(new Integer[] {5, 2});
        pq.offer(new Integer[] {3, 3});
        pq.offer(new Integer[] {1, 4});
        pq.offer(new Integer[] {1, 5});
        pq.offer(new Integer[] {7, 5});
        while(!pq.isEmpty()) {
            System.out.println(Arrays.toString(pq.poll()));
        }

        // 배열 슬라이싱 ----------------------------------------
        // copyOfRange 메소드 활용
        int[] srcArray = IntStream.rangeClosed(1,10).toArray();
        int[] destArray = Arrays.copyOfRange(srcArray,3,7);
        System.out.println("srcArray : " + Arrays.toString(srcArray));
        System.out.println("destArray : " + Arrays.toString(destArray));
        //Stream API 활용
        int[] destArray2 = IntStream.range(3,7).map(num -> srcArray[num]).toArray();
        System.out.println("destArray2 : " + Arrays.toString(destArray2));

        // List 슬라이싱 ---------------------------------------
        List<Integer> intArrayList = new ArrayList<>(Arrays.asList(10,0,1,2,3,4,5,6));
        List<Integer> newList = new ArrayList<>(intArrayList.subList(2,5));
        Collections.sort(intArrayList);
        System.out.println("newList : " + newList);
        System.out.println("intArrayList : " + intArrayList);
        intArrayList = new ArrayList<>(intArrayList.subList(0,3));
        intArrayList.sort(Comparator.reverseOrder());
        System.out.println("reverseOrder intArrayList : " + intArrayList);
        intArrayList.sort(Comparator.comparingInt(o -> o));
        intArrayList.sort(Integer::compare);
        System.out.println("newList : " + newList);
        System.out.println("intArrayList : " + intArrayList);

        // String 자르기
        String str1 = "ABCDEF";
        String str2 = "010-3478-3315";
        String str3 = "바나나 : 1000원, 사과 : 2000원, 배 : 3000원";

        String cutStr1 = str1.substring(str1.length()- 3);
        System.out.println("cutStr1 : " + cutStr1);

        String cutStr2 = String.join("", str2.split("-"));
        System.out.println("cutStr2 : " + cutStr2);

        String cutStr3 = str3.substring(str3.indexOf("사과"), str3.substring(str3.indexOf("사과")).indexOf("원") + str3.indexOf("사과"));
        System.out.println("cutStr3 : " + cutStr3 + "원");

        // 구조 분해 할당 ---------------------------------------
        //

    }

}
