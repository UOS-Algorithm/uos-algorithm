import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj2671 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String pattern = "^(100+1+|01)+$";

        String input = br.readLine();

        if (input.matches(pattern)) {
            System.out.println("SUBMARINE");
        } else {
            System.out.println("NOISE");
        }
    }
}
