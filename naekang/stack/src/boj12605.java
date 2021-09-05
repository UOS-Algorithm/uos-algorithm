import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj12605 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= T; i++) {
            String[] str = br.readLine().split(" ");
            StringBuilder sbr = new StringBuilder();

            for (int j = str.length - 1; j >= 0; j--) {
                sbr.append(str[j]).append(" ");
            }
            sb.append("Case #").append(i).append(": ").append(sbr).append("\n");
        }
        System.out.println(sb.toString());

    }
}
