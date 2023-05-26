package 연습문제.푸드파이트대회;

import java.util.stream.IntStream;

public class Solution {
    public String solution1(int[] food) { // 첫번째 풀이
        /*
            food[i] -> 음식 i의 준비된 개수
            food[i] < i 보다 작은 경우 음식을 준비할 수 없음
         */
        StringBuilder result = new StringBuilder();
        int a = 1;
        IntStream.range(0, food.length)
                .skip(1)
                .forEach(idx -> {
                    result.append(String.valueOf(idx).repeat(food[idx] / 2));
                });
        result.append(0);
        result.append(new StringBuilder(result.substring(0,result.length() - 1)).reverse());
        return result.toString();
    }
    public String solution(int[] food) { // 첫번째 풀이
        /*
            food[i] -> 음식 i의 준비된 개수
            food[i] < i 보다 작은 경우 음식을 준비할 수 없음
         */
        StringBuilder result = new StringBuilder();
        IntStream.range(0, food.length)
                .skip(1)
                .forEach(idx -> {
                    result.append(String.valueOf(idx).repeat(food[idx] / 2));
                });
        return result.toString() + "0" + result.reverse().toString();
    }
}
