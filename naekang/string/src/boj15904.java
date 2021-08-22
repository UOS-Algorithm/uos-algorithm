import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj15904 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] str = br.readLine().split("");

        int index = 0;
        for (String ch : str) {
            if (index == 0 && ch.equals("U"))
                index++;
            if ((index == 1 || index == 3) && ch.equals("C"))
                index++;
            if (index == 2 && ch.equals("P"))
                index++;
        }

        System.out.println((index == 4) ? "I love UCPC" : "I hate UCPC");
    }
}
