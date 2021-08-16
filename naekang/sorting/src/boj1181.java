import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class boj1181 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        String[] words = new String[N];

        sc.nextLine();

        for (int i = 0; i < N; i++) {
            words[i] = sc.nextLine();
        }

        Arrays.sort(words, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                if (o1.length() == o2.length()) {
                    return o1.compareTo(o2);
                } else {
                    return o1.length() - o2.length();
                }
            }
        });

        System.out.println(words[0]);

        for (int i = 1; i < N; i++) {
            if (!words[i].equals(words[i - 1])) {
                System.out.println(words[i]);
            }
        }
    }
}
