import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class boj20001 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Stack<Boolean> stack = new Stack<Boolean>();

        while (true) {
            String str = br.readLine();

            if (str.equals("고무오리")) {
                if (stack.size() == 0) {
                    stack.push(true);
                    stack.push(true);
                } else
                    stack.pop();
            } else if (str.equals("문제")) {
                stack.push(true);
            } else if (str.equals("고무오리 디버깅 끝")) {
                break;
            }
        }

        System.out.println(stack.isEmpty() ? "고무오리야 사랑해" : "힝구");
    }
}
