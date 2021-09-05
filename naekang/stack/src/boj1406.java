import java.io.*;
import java.util.Stack;

public class boj1406 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String str = br.readLine();
        int M = Integer.parseInt(br.readLine());

        Stack<Character> lstack = new Stack<>();
        Stack<Character> rstack = new Stack<>();

        for (int i = 0; i < str.length(); i++) {
            lstack.push(str.charAt(i));
        }

        while (M-- > 0) {
            String[] word = br.readLine().split(" ");

            if (word[0].equals("L") && !lstack.isEmpty()) {
                rstack.push(lstack.pop());
            } else if (word[0].equals("D") && !rstack.isEmpty()) {
                lstack.push(rstack.pop());
            } else if (word[0].equals("B") && !lstack.isEmpty()) {
                lstack.pop();
            } else if (word[0].equals("P")) {
                lstack.push(word[1].charAt(0));
            }
        }

        while (!lstack.isEmpty()) {
            rstack.push(lstack.pop());
        }
        while (!rstack.isEmpty()) {
            sb.append(rstack.pop());
        }
        System.out.println(sb);
    }
}
