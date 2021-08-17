import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj1013 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            String str = br.readLine().trim();
            String pattern = "(100+1+|01)+";
            if (str.matches(pattern))
                System.out.println("YES");
            else
                System.out.println("NO");
        }
    }
}
