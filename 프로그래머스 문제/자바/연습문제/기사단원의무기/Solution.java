package 연습문제.기사단원의무기;

import java.util.stream.IntStream;

public class Solution {
//    public int solution(int number, int limit, int power) {
//        return IntStream.rangeClosed(1,number).map(num -> {
//            int temp = calPrimeNum(num);
//            if (temp > limit) {
//                return power;
//            }else {
//                return temp;
//            }
//        }).sum();
//    }
    public int solution(int number, int limit, int power) {
        int[] count = new int[number + 1];
        for (int i = 1; i <= number; i++) {
            for (int j = 1; j <= number / i; j++) {
                count[i * j]++;
            }
        }
        int answer = 0;
        for (int i = 1; i <= number; i++) {
            if (count[i] > limit) {
                answer += power;
            } else {
                answer += count[i];
            }
        }
        return answer;
    }
    private int calPrimeNum(int target) {
        return IntStream.rangeClosed(1,(int)Math.sqrt(target)).map(num -> {
                if (target % num == 0) {
                    if (Math.pow(num, 2) == target)
                        return 1;
                    return 2;
                }
                return 0; 
        }).sum();
    }
}
