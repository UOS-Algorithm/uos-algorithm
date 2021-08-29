import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class boj2812 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        Deque<Character> dq = new ArrayDeque<>();

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        String str = br.readLine();

        char[] arr = str.toCharArray();

        for (int i = 0; i < str.length(); i++) {
            while (K > 0 && dq.size() > 0 && dq.getLast() < arr[i]) {
                dq.removeLast();
                K--;
            }
            dq.addLast(arr[i]);
        }

        StringBuilder sb = new StringBuilder();

        while (dq.size() > K) {
            sb.append(dq.removeFirst());
        }

        System.out.println(sb.toString());
    }
}
