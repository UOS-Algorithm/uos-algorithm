import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class boj5052 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            String[] phone = new String[n];

            for (int i = 0; i < n; i++) {
                phone[i] = br.readLine();
            }

            Arrays.sort(phone);

            if (check(n, phone))
                System.out.println("YES");
            else
                System.out.println("NO");
        }


    }
    static boolean check (int n, String[] phone) {
        for (int i = 0; i < n - 1; i++) {
            if (phone[i+1].startsWith(phone[i]))
                return false;
        }
        return true;
    }
}
