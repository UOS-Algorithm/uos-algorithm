import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj1120 {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");

        System.out.println(solve(input[0], input[1]));
    }

    static int solve(String str1, String str2) {
        int min = Integer.MAX_VALUE;

        for (int i = 0; i <= str2.length() - str1.length(); i++) {
            int cnt = 0;
            for (int j = 0; j < str1.length(); j++) {
                if (str1.charAt(j) != str2.charAt(i + j)) {
                    cnt++;
                }
            }
            if (cnt < min) {
                min = cnt;
            }
        }
        return min;
    }
}
