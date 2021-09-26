import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class boj1012 {
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int[][] arr;
    static int n, m, k, cnt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            String str[] = br.readLine().split(" ");
            m = Integer.parseInt(str[0]);
            n = Integer.parseInt(str[1]);
            k = Integer.parseInt(str[2]);
            cnt = 0;
            arr = new int[n][m];

            for (int j = 0; j < k; j++) {
                str = br.readLine().split(" ");
                arr[Integer.parseInt(str[1])][Integer.parseInt(str[0])] = 1;
            }

            for (int x = 0; x < n; x++) {
                for (int y = 0; y < m; y++) {
                    if (arr[x][y] != 0) {
                        dfs(x, y);
                        cnt++;
                    }
                }
            }
            System.out.println(cnt);
        }
    }

    public static void dfs(int x, int y) {
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                continue;
            }
            if (arr[nx][ny] == 0) {
                continue;
            }
            arr[nx][ny] = 0;
            dfs(nx, ny);
        }
    }
}
