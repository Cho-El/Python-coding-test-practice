package 연습문제.햄버거만들기;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;
        /*
            빵 순서는 1 2 3 1로
            1 일떄는 3을 뺴야함
            3 일 떄는 2
            2 일 때는 1
         */
        Map<Integer,Integer> pair = new HashMap<>() {{
            put(1, 3);
            put(2, 1);
            put(3, 2);
        }};
        Stack<Integer> stack = new Stack<>();
        for (int ing : ingredient) {
            if (stack.size() < 3 || ing != 1) {
                stack.push(ing);
            } else {
               Stack<Integer> burgerPossible = new Stack<>();
               burgerPossible.push(ing);
               while (!stack.empty() && burgerPossible.size() != 4) {
                   if (pair.get(burgerPossible.peek()) == stack.peek()) {
                       burgerPossible.push(stack.pop());
                   } else {
                       //
                       while (!burgerPossible.empty()) {
                           stack.push(burgerPossible.pop());
                       }
                       break;
                   }
               }
               if (burgerPossible.size() == 4)
                   answer ++;
            }
        }
        return answer;
    }
}