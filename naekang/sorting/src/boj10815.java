import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.StringTokenizer;

public class boj10815 {

    static int N, M;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < M; i++) {
            int num = Integer.parseInt(st.nextToken());

            if (search(num)) {
                System.out.print("1 ");
            } else {
                System.out.print("0 ");
            }
        }

    }

    static boolean search(int x) {
        int left = 0;
        int right = N - 1;

        while (left <= right) {
            int midInx = (left + right) / 2;
            int mid = arr[midInx];

            if (x < mid) {
                right = midInx - 1;
            } else if (x > mid) {
                left = midInx + 1;
            } else {
                return true;
            }
        }
        return false;
    }
}
