import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj14490 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), ":");

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int gcd = GCD(n, m);

        System.out.println(n/gcd + ":" + m/gcd);

    }

    static int GCD(int n, int m) {
        if (m == 0)
            return n;
        return GCD(m, n % m);
    }
}
