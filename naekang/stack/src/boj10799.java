import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class boj10799 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();

        Stack<Character> stack = new Stack<>();

        int cnt = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '(') {
                stack.push('(');
                continue;
            }
            if (str.charAt(i) == ')') {
                stack.pop();

                if (str.charAt(i - 1) == '(') {
                    cnt += stack.size();
                } else {
                    cnt++;
                }
            }
        }
        System.out.println(cnt);
    }
}
